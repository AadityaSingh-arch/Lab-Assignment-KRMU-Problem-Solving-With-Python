import os
import pandas as pd
import matplotlib.pyplot as plt

# GET SCRIPT FOLDER
BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "data")
OUTPUT = os.path.join(BASE, "output")

os.makedirs(OUTPUT, exist_ok=True)

print("Using data folder:", DATA)

# FIND ALL CSV FILES
files = []
for f in os.listdir(DATA):
    if f.endswith(".csv"):
        files.append(os.path.join(DATA, f))

if not files:
    print("❌ No CSV files found inside data folder!")
    exit()

# READ FILES SAFELY
all_data = []

for file in files:
    try:
        df = pd.read_csv(file)

        if df.empty:
            print(f"⚠️ Empty file skipped: {file}")
            continue

        df["building"] = os.path.basename(file).replace(".csv", "")
        all_data.append(df)
        print(f"✅ Loaded {file}")

    except Exception as e:
        print(f"❌ Failed to read {file} → {e}")

# COMBINE DATA
df_all = pd.concat(all_data, ignore_index=True)

# SAVE CLEANED FILE
df_all.to_csv(os.path.join(OUTPUT, "cleaned_energy_data.csv"), index=False)

# ANALYSIS
total = df_all["kwh"].sum()
per_building = df_all.groupby("building")["kwh"].sum()
per_type = df_all.groupby("type")["kwh"].sum()

per_building.to_csv(os.path.join(OUTPUT, "building_summary.csv"))

# REPORT FILE
with open(os.path.join(OUTPUT, "summary.txt"), "w") as f:
    f.write("CAMPUS ENERGY SUMMARY\n")
    f.write("=====================\n\n")
    f.write(f"Total usage: {total} kWh\n\n")

    f.write("Per Building:\n")
    f.write(str(per_building) + "\n\n")

    f.write("Per Type:\n")
    f.write(str(per_type))

# PLOTS
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
per_building.plot(kind="bar")
plt.title("Building Consumption")

plt.subplot(1,2,2)
per_type.plot(kind="bar")
plt.title("Type Consumption")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT, "dashboard.png"))
plt.close()

print("\n✅ SUCCESS. ALL OUTPUT GENERATED:")
print(" - cleaned_energy_data.csv")
print(" - building_summary.csv")
print(" - summary.txt")
print(" - dashboard.png")

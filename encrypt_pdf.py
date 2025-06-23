import pikepdf
import os

# --- File Paths ---
input_pdf = r"C:\Users\bstSt\AppData\Local\FoundryVTT\Data\systems\monsterhighrpg\source\MonsterHighschoolRPG.pdf"
output_pdf = r"C:\Users\bstSt\AppData\Local\FoundryVTT\Data\systems\monsterhighrpg\assets\MonsterHighschoolRPG_encrypted.pdf"

# --- Passwords ---
user_password = "monsterhigh_access"
owner_password = "MonsterHighschoolRPG"

# --- Define allowed permissions (we allow NOTHING here) ---
# For example, if you wanted to allow printing, you'd do:
# permissions = pikepdf.Permissions(pikepdf.Permissions.printing)
# But to restrict everything:
permissions = pikepdf.Permissions()  # No permissions granted

# --- Ensure output directory exists ---
output_dir = os.path.dirname(output_pdf)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"📂 Created folder: {output_dir}")

# --- Check if input file exists ---
if not os.path.isfile(input_pdf):
    print(f"❌ ERROR: Input file does not exist at: {input_pdf}")
    exit(1)

# --- Encrypt the PDF ---
try:
    with pikepdf.open(input_pdf) as pdf:
        pdf.save(
            output_pdf,
            encryption=pikepdf.Encryption(
                user=user_password,
                owner=owner_password,
                allow=permissions,
                R=4
            )
        )
    print(f"✅ Encrypted PDF saved at: {output_pdf}")

except Exception as e:
    print(f"❌ Encryption failed: {e}")

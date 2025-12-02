import os

print("=" * 60)
print("DIAGNOSTIC DE L'ARBORESCENCE")
print("=" * 60)

# Test 1 : BASE_PATH existe ?
print(f"\n1. BASE_PATH = {BASE_PATH}")
print(f"   Existe ? {os.path.exists(BASE_PATH)}")
print(f"   Chemin absolu : {os.path.abspath(BASE_PATH)}")

# Test 2 : Contenu de BASE_PATH
if os.path.exists(BASE_PATH):
    print(f"\n2. Contenu de BASE_PATH :")
    try:
        items = os.listdir(BASE_PATH)
        for item in items:
            full = os.path.join(BASE_PATH, item)
            type_str = "DIR" if os.path.isdir(full) else "FILE"
            print(f"   [{type_str}] {item}")
    except Exception as e:
        print(f"   ❌ Erreur : {e}")
else:
    print(f"\n2. ❌ BASE_PATH n'existe pas !")

# Test 3 : Dossier geometry
geometry_path = os.path.join(BASE_PATH, "geometry")
print(f"\n3. Dossier geometry :")
print(f"   Chemin : {geometry_path}")
print(f"   Existe ? {os.path.exists(geometry_path)}")

if os.path.exists(geometry_path):
    print(f"   Contenu :")
    for root, dirs, files in os.walk(geometry_path):
        print(f"     Root: {root}")
        print(f"     Dirs: {dirs}")
        print(f"     Files: {files}")

# Test 4 : Dossier physics
physics_path = os.path.join(BASE_PATH, "physics")
print(f"\n4. Dossier physics :")
print(f"   Chemin : {physics_path}")
print(f"   Existe ? {os.path.exists(physics_path)}")

if os.path.exists(physics_path):
    print(f"   Contenu :")
    for root, dirs, files in os.walk(physics_path):
        print(f"     Root: {root}")
        print(f"     Dirs: {dirs}")
        print(f"     Files: {files}")

# Test 5 : Simulation de list_files
print(f"\n5. Simulation de list_files('geometry') :")

def list_files_test(path: str):
    result = []
    full_path = BASE_PATH + path
    print(f"   Chemin complet : {full_path}")
    
    for root, dirs, files in os.walk(full_path):
        for f in files:
            result.append(os.path.join(root, f))
    
    return result

files = list_files_test("geometry")
print(f"   Résultat : {files}")
print(f"   Nombre de fichiers : {len(files)}")

print("\n" + "=" * 60)
print("FIN DU DIAGNOSTIC")
print("=" * 60)
poetry build
pip uninstall --yes remi-portal-gun
pip install ../dist/remi_portal_gun-0.3.0-py3-none-any.whl 
remi-portal-gun

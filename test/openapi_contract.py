import glob
import yaml
from openapi_spec_validator import validate_spec


def test_openapi_specs_load_and_validate():
    files = glob.glob('docs/api/**/*.yaml', recursive=True)
    assert files, "No OpenAPI YAML files found under docs/api/"
    errors = []
    for f in files:
        with open(f, 'r') as fh:
            spec = yaml.safe_load(fh)
        try:
            validate_spec(spec)
        except Exception as e:
            errors.append(f"{f}: {e}")
    assert not errors, "OpenAPI validation errors:\n" + "\n".join(errors)

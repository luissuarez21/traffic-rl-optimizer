"""Quick test that packages installed correctly."""
import os
import sys

def test_imports():
    """Test all required imports."""
    errors = []
    successes = []
    
    print("="*60)
    print("Testing Package Imports")
    print("="*60)
    
    # Test SUMO
    try:
        import traci
        successes.append("✓ TraCI (SUMO Python interface)")
    except ImportError as e:
        errors.append(f"✗ TraCI: {e}")
    
    # Test RL frameworks
    try:
        import gymnasium
        successes.append(f"✓ Gymnasium v{gymnasium.__version__}")
    except ImportError as e:
        errors.append(f"✗ Gymnasium: {e}")
    
    try:
        from stable_baselines3 import PPO
        import stable_baselines3
        successes.append(f"✓ Stable-Baselines3 v{stable_baselines3.__version__}")
    except ImportError as e:
        errors.append(f"✗ Stable-Baselines3: {e}")
    
    # Test ML frameworks
    try:
        import torch
        successes.append(f"✓ PyTorch v{torch.__version__}")
    except ImportError as e:
        errors.append(f"✗ PyTorch: {e}")
    
    try:
        import xgboost
        successes.append(f"✓ XGBoost v{xgboost.__version__}")
    except ImportError as e:
        errors.append(f"✗ XGBoost: {e}")
    
    try:
        import sklearn
        successes.append(f"✓ Scikit-learn v{sklearn.__version__}")
    except ImportError as e:
        errors.append(f"✗ Scikit-learn: {e}")
    
    # Test data science
    try:
        import numpy
        successes.append(f"✓ NumPy v{numpy.__version__}")
    except ImportError as e:
        errors.append(f"✗ NumPy: {e}")
    
    try:
        import pandas
        successes.append(f"✓ Pandas v{pandas.__version__}")
    except ImportError as e:
        errors.append(f"✗ Pandas: {e}")
    
    # Test visualization
    try:
        import matplotlib
        successes.append(f"✓ Matplotlib v{matplotlib.__version__}")
    except ImportError as e:
        errors.append(f"✗ Matplotlib: {e}")
    
    try:
        import plotly
        successes.append(f"✓ Plotly v{plotly.__version__}")
    except ImportError as e:
        errors.append(f"✗ Plotly: {e}")
    
    # Test web framework
    try:
        import flask
        successes.append(f"✓ Flask v{flask.__version__}")
    except ImportError as e:
        errors.append(f"✗ Flask: {e}")
    
    # Check SUMO environment variable
    print("\n" + "="*60)
    print("Checking SUMO Configuration")
    print("="*60)
    
    sumo_home = os.environ.get('SUMO_HOME')
    if sumo_home:
        successes.append(f"✓ SUMO_HOME = {sumo_home}")
        
        # Check if SUMO binary exists
        if sys.platform == "win32":
            sumo_binary = os.path.join(sumo_home, "bin", "sumo.exe")
        else:
            sumo_binary = os.path.join(sumo_home, "bin", "sumo")
        
        if os.path.exists(sumo_binary):
            successes.append(f"✓ SUMO binary found: {sumo_binary}")
        else:
            errors.append(f"✗ SUMO binary not found at: {sumo_binary}")
    else:
        errors.append("✗ SUMO_HOME environment variable not set")
    
    # Print results
    print("\n" + "="*60)
    print("Results")
    print("="*60)
    
    if successes:
        print("\n✅ Successful:")
        for success in successes:
            print(f"  {success}")
    
    if errors:
        print("\n❌ Failed:")
        for error in errors:
            print(f"  {error}")
        print("\n" + "="*60)
        print("⚠️  Setup incomplete - see errors above")
        print("="*60)
        return False
    else:
        print("\n" + "="*60)
        print("✅ ALL CHECKS PASSED!")
        print("="*60)
        print("\n🚀 You're ready to start building!")
        print("\nNext step: Create your first SUMO simulation")
        return True

if __name__ == "__main__":
    success = test_imports()
    sys.exit(0 if success else 1)
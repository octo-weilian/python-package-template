from my_app import LOGGER,CONFIG,INI_FILE
import sys

def main():
    LOGGER.info(f"Input arguments: {sys.argv[1:]}")
    LOGGER.info(f"Set parameters in {INI_FILE}:")
    
    for k,v in dict(CONFIG["section"]).items():
        print(f"{k:10}:{v}")
    
if __name__ == "__main__":
    
    main()
    
    
    
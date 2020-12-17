package kishocinema;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.List;
import java.util.HashMap;
import parser.Values;
import parser.ast.ModulesFile;
import parser.ast.PropertiesFile;
import prism.Prism;
import prism.PrismDevNullLog;
import prism.PrismException;
import prism.PrismLog;
import prism.Result;
import prism.UndefinedConstants;

public class CheckKishoModel {
  
  private static HashMap<String, Integer> states = new HashMap<>();
  
  public static void main(String[] args) {
      new CheckKishoModel().run();
  }

  public void run() {
    
    states.put("IDLE", 1);
    states.put("NORMAL", 2);
    states.put("OVERLOADED", 3);
    states.put("CRITICAL", 4);
    states.put("FAILED", 5);
    
    try {
      // Create a log for PRISM output (hidden or stdout)
      PrismLog mainLog = new PrismDevNullLog();
      // PrismLog mainLog = new PrismFileLog("stdout");

      // Initialise PRISM engine
      Prism prism = new Prism(mainLog);
      prism.initialise();

      // Parse and load a PRISM model from a file
      ModulesFile modulesFile =
          prism.parseModelFile(new File("../models/kisho.pm"));
      prism.loadPRISMModel(modulesFile);

      // Model check a property specified as a string
      for (String stateName : states.keySet()) {
        Integer stateLevel = states.get(stateName);
        String property = "P=? [ F=10 s=" + stateLevel + " ]";
        Result result = prism.modelCheck(property);
        System.out.println(stateName + ": " + result.getResult());
      }

      // Close down PRISM
      prism.closeDown();

    } catch (FileNotFoundException e) {
      System.out.println("Error: " + e.getMessage());
      System.exit(1);
    } catch (PrismException e) {
      System.out.println("Error: " + e.getMessage());
      System.exit(1);
    }
  }
}
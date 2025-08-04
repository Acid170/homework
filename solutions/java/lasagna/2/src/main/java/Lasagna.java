public class Lasagna {

    public int expectedMinutesInOven(){
        return 40;
    }


    public int remainingMinutesInOven(int actualMinutes){
        return  expectedMinutesInOven() - actualMinutes;
    }


    public int preparationTimeInMinutes(int numOfLayers){
        return numOfLayers * 2;
    }


    public int totalTimeInMinutes(int numOfLayers, int actualMinutes){
        return (actualMinutes + preparationTimeInMinutes(numOfLayers)); 
    }
}

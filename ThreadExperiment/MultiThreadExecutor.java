import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;

public class MultiThreadExecutor {

    public static void runMultiThread() throws Exception {
        long START = 0;
        long END = 100_000_000L;

        int NUM_TASKS = Runtime.getRuntime().availableProcessors();
        System.out.println("Number of available processors: " + NUM_TASKS);

        long chunkSize = (END - START) / NUM_TASKS;

        ExecutorService executor = Executors.newFixedThreadPool(NUM_TASKS);
        List<Future<Long>> futures = new ArrayList<>();

        long startTime = System.currentTimeMillis();

        for (int i = 0; i < NUM_TASKS; i++) {
            long rangeStart = START + i * chunkSize;
            long rangeEnd = (i == NUM_TASKS - 1) ? END : rangeStart + chunkSize;

         
            futures.add(executor.submit(() -> Main.cpuIntensiveTask(rangeStart, rangeEnd)));
        }

        long totalSum = 0;
        for (Future<Long> f : futures) {
            totalSum += f.get(); 
        }

        executor.shutdown();

        long endTime = System.currentTimeMillis();
        
        System.out.println("Execution Time = " + (endTime - startTime) + " ms");
    }

}

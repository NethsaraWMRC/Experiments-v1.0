public class SingleThread {
    public SingleThread() {
        long startTime = System.currentTimeMillis();
        Main.cpuIntensiveTask(1, 100_000_000L);
        long endTime = System.currentTimeMillis();
        System.out.println("SingleThread Execution Time: " + (endTime - startTime) + " ms");
    }
}

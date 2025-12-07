public class Main {
    public static void main(String[] args) {
        new SingleThread();
        new MultiThread();

        try {
            MultiThreadExecutor.runMultiThread();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    // cpu task
    public static long cpuIntensiveTask(long start, long end) {
        long sum = 0;
        for (long i = start; i < end; i++) {
            sum += Math.pow(i,4);
        }
        return sum;
    }
}
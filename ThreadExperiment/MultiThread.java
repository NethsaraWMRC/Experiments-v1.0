public class MultiThread {
    public MultiThread() {
        Thread thread1 = new Thread(() -> Main.cpuIntensiveTask(0, 50_000_000L));
        Thread thread2 = new Thread(() -> Main.cpuIntensiveTask(50_000_000L, 100_000_000L));

        long startTime = System.currentTimeMillis();

        thread1.start();
        thread2.start();

        try {
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        long endTime = System.currentTimeMillis();
        System.out.println("MultiThread Execution Time: " + (endTime - startTime) + " ms");
    }
}

public class test_java {
	public static void main(String args[]){
		long start_time = System.currentTimeMillis();
		long x;
		for(long i = 0; i < 100000000L; i++){
			x = i * i;
		}
		long end_time = System.currentTimeMillis();
		long total_time = end_time - start_time;
		System.out.println("Program execution time:");
		System.out.println("--- " + (float) total_time/1000 + " seconds ---");
	}
}

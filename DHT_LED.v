module temperature_led_blink(
    input wire clk,      // Clock signal
    output reg led0,    // LED 0 output
    output reg led1,    // LED 1 output
    output reg led2,    // LED 2 output
    output reg dht22_trigger // Trigger signal for DHT22 sensor (connected to Arduino header pin)
   
);

// Define temperature range thresholds (adjust these values as needed)
parameter LOW_THRESHOLD = 8'b11001;  // 25 degrees in binary
parameter MID_THRESHOLD = 8'b11110;  // 30 degrees in binary
parameter HIGH_THRESHOLD = 8'b100011; // 35 degrees in binary

reg [7:0] temperature_counter;

always @(posedge clk) begin
    // Increment the temperature counter (simulated temperature reading)
    temperature_counter <= temperature_counter + 1'b1;

    // Check temperature counter against predefined thresholds
    if (temperature_counter < LOW_THRESHOLD)
    begin
        led0 <= 1'b1; // LED 0 is on
        led1 <= 1'b0; // LED 1 is off
        led2 <= 1'b0; // LED 2 is off
    end
    else if (temperature_counter < MID_THRESHOLD)
    begin
        led0 <= 1'b0; // LED 0 is off
        led1 <= 1'b1; // LED 1 is on
        led2 <= 1'b0; // LED 2 is off
    end
    else if (temperature_counter < HIGH_THRESHOLD)
    begin
        led0 <= 1'b0; // LED 0 is off
        led1 <= 1'b0; // LED 1 is off
        led2 <= 1'b1; // LED 2 is on
    end
    else
    begin
        led0 <= 1'b0; // All LEDs are off
        led1 <= 1'b0;
        led2 <= 1'b0;
    end
end

// Generate trigger signal for DHT22 sensor (modify pin assignment as needed)
always @(posedge clk) begin
    // Toggle the trigger signal to the DHT22 sensor
    dht22_trigger <= ~dht22_trigger;
end

endmodule

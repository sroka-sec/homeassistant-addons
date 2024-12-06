document.getElementById("configForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const mainMeter = document.getElementById("mainMeter").value;
  const devices = document.getElementById("devices").value.split("\n").map(device => device.trim());

  const response = await fetch("/config", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ main_meter: mainMeter, devices_to_control: devices })
  });

  if (response.ok) {
    alert("Configuration saved successfully!");
  } else {
    alert("Failed to save configuration. Please try again.");
  }
});

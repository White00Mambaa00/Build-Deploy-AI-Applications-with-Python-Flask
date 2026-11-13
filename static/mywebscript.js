"use strict";

// The course template calls this global function from its analyze button.
async function RunSentimentAnalysis() {
  const text = document.getElementById("textToAnalyze").value;
  const output = document.getElementById("system_response");
  const status = document.getElementById("analysisStatus");
  const button = document.getElementById("analyzeButton");
  status.textContent = "Analyzing…";
  output.textContent = "Contacting the emotion detection service…";
  button.disabled = true;
  try {
    const url = "/emotionDetector?textToAnalyze=" + encodeURIComponent(text);
    const response = await fetch(url);
    output.textContent = await response.text();
    status.textContent = response.ok ? "Analysis complete" : "Service error";
  } catch (error) {
    output.textContent = "Unable to contact the server. Please try again.";
    status.textContent = "Connection error";
  } finally {
    button.disabled = false;
  }
}

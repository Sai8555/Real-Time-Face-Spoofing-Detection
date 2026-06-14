// // // document.addEventListener('DOMContentLoaded', () => {
// //     const startLivenessButton = document.getElementById('start-liveness-btn');
// //     const stopLivenessButton = document.getElementById('stop-liveness-btn');

// //     async function startLivenessTesting() {
// //         const response = await fetch('/start_liveness', { method: 'POST' });
// //         if (response.ok) {
// //             startLivenessButton.disabled = true;
// //             stopLivenessButton.disabled = false;
// //         } else {
// //             alert("Failed to start liveness testing.");
// //         }
// //     }

// //     async function stopLivenessTesting() {
// //         const response = await fetch('/stop_liveness', { method: 'POST' });
// //         if (response.ok) {
// //             startLivenessButton.disabled = false;
// //             stopLivenessButton.disabled = true;
// //         } else {
// //             alert("Failed to stop liveness testing.");
// //         }
// //     }

// //     startLivenessButton.addEventListener('click', startLivenessTesting);
// //     stopLivenessButton.addEventListener('click', stopLivenessTesting);

// //     const getStartedButton = document.getElementById('get-started-btn');
// //     if (getStartedButton) {
// //         getStartedButton.addEventListener('click', () => {
// //             window.location.href = '/detection';
// //         });
// //     }
// //     function pollStatus() {
// //         const statusText = document.getElementById('status-text');
    
// //         const intervalId = setInterval(async () => {
// //             const response = await fetch('/status');
// //             const data = await response.json();
    
// //             statusText.textContent = data.status;
    
// //             if (data.status === 'Live Face Confirmed') {
// //                 clearInterval(intervalId);
// //                 stopLivenessTesting();  // Optionally stop stream
// //             }
// //         }, 1000); // Check every second
// //     }
// //     async function startLivenessTesting() {
// //         const response = await fetch('/start_liveness', { method: 'POST' });
// //         if (response.ok) {
// //             startLivenessButton.disabled = true;
// //             stopLivenessButton.disabled = false;
// //             pollStatus();  // Start polling the server for result
// //         } else {
// //             alert("Failed to start liveness testing.");
// //         }
// //     }
    
// // // });






// // // document.addEventListener('DOMContentLoaded', () => {
// // //     const startLivenessButton = document.getElementById('start-liveness-btn');
// // //     const stopLivenessButton = document.getElementById('stop-liveness-btn');

// // //     startLivenessButton.addEventListener('click', async () => {
// // //         const response = await fetch('/start_liveness', { method: 'POST' });
// // //         if (response.ok) {
// // //             console.log("Started");
// // //             startLivenessButton.disabled = true;
// // //             stopLivenessButton.disabled = false;
// // //         }
// // //     });

// // //     stopLivenessButton.addEventListener('click', () => {
// // //         fetch('/stop_liveness', { method: 'POST' })
// // //             .then(() => {
// // //                 startLivenessButton.disabled = false;
// // //                 stopLivenessButton.disabled = true;
// // //             });
// // //     });

// // //     document.getElementById('get-started-btn').addEventListener('click', () => {
// // //         window.location.href = '/detection';
// // //     });
// // // });


// // document.addEventListener('DOMContentLoaded', () => {
// //     const startLivenessButton = document.getElementById('start-liveness-btn');
// //     const stopLivenessButton = document.getElementById('stop-liveness-btn');
// //     const statusText = document.getElementById('status-text');
// //     const getStartedButton = document.getElementById('get-started-btn');

// //     let pollingInterval = null;

// //     async function startLivenessTesting() {
// //         const response = await fetch('/start_liveness', { method: 'POST' });
// //         if (response.ok) {
// //             startLivenessButton.disabled = true;
// //             stopLivenessButton.disabled = false;
// //             statusText.textContent = "Detecting...";
// //             startPollingStatus();
// //         } else {
// //             alert("Failed to start liveness testing.");
// //         }
// //     }

// //     async function stopLivenessTesting() {
// //         const response = await fetch('/stop_liveness', { method: 'POST' });
// //         if (response.ok) {
// //             startLivenessButton.disabled = false;
// //             stopLivenessButton.disabled = true;
// //             statusText.textContent = "Start";
// //             stopPollingStatus();
// //         } else {
// //             alert("Failed to stop liveness testing.");
// //         }
// //     }

// //     function startPollingStatus() {
// //         stopPollingStatus(); // Prevent multiple intervals
// //         pollingInterval = setInterval(async () => {
// //             const response = await fetch('/status');
// //             const data = await response.json();
// //             statusText.textContent = data.status;

// //             if (data.status === 'Live Face Confirmed') {
// //                 stopPollingStatus();
// //                 stopLivenessTesting(); // Stop the video stream
// //             }
// //         }, 1000);
// //     }

// //     function stopPollingStatus() {
// //         if (pollingInterval !== null) {
// //             clearInterval(pollingInterval);
// //             pollingInterval = null;
// //         }
// //     }

// //     startLivenessButton.addEventListener('click', startLivenessTesting);
// //     stopLivenessButton.addEventListener('click', stopLivenessTesting);

// //     if (getStartedButton) {
// //         getStartedButton.addEventListener('click', () => {
// //             window.location.href = '/detection';
// //         });
// //     }
// // });

// document.addEventListener('DOMContentLoaded', () => {
//     const startLivenessButton = document.getElementById('start-liveness-btn');
//     const stopLivenessButton = document.getElementById('stop-liveness-btn');
//     const statusText = document.getElementById('status-text');
//     const getStartedButton = document.getElementById('get-started-btn');
//     const videoFeed = document.getElementById('video-feed');
    
//     let pollingInterval = null;
    
//     // Initialize buttons
//     if (startLivenessButton && stopLivenessButton) {
//         startLivenessButton.disabled = false;
//         stopLivenessButton.disabled = true;
//     }
    
//     // Function to refresh the video feed
//     function refreshVideoFeed() {
//         if (videoFeed) {
//             const timestamp = new Date().getTime();
//             videoFeed.src = `/video_feed?t=${timestamp}`;
//         }
//     }
    
//     async function startLivenessTesting() {
//         try {
//             const response = await fetch('/start_liveness', { 
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                     'Cache-Control': 'no-cache'
//                 }
//             });
            
//             const data = await response.json();
            
//             if (data.status === 'success') {
//                 startLivenessButton.disabled = true;
//                 stopLivenessButton.disabled = false;
//                 statusText.textContent = "Detecting...";
                
//                 // Refresh the video feed
//                 refreshVideoFeed();
                
//                 // Start polling for status updates
//                 startPollingStatus();
//             } else {
//                 alert("Failed to start liveness testing: " + (data.message || "Unknown error"));
//             }
//         } catch (error) {
//             console.error("Error starting liveness testing:", error);
//             alert("Error starting liveness testing. Check console for details.");
//         }
//     }
    
//     async function stopLivenessTesting() {
//         try {
//             const response = await fetch('/stop_liveness', { 
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                     'Cache-Control': 'no-cache'
//                 }
//             });
            
//             const data = await response.json();
            
//             if (data.status === 'success') {
//                 startLivenessButton.disabled = false;
//                 stopLivenessButton.disabled = true;
//                 stopPollingStatus();
//             } else {
//                 alert("Failed to stop liveness testing.");
//             }
//         } catch (error) {
//             console.error("Error stopping liveness testing:", error);
//         }
//     }
    
//     function startPollingStatus() {
//         stopPollingStatus(); // Prevent multiple intervals
        
//         // Immediately check status once
//         checkStatus();
        
//         pollingInterval = setInterval(checkStatus, 1000);
//     }
    
//     async function checkStatus() {
//         try {
//             const response = await fetch('/status', {
//                 headers: {
//                     'Cache-Control': 'no-cache'
//                 }
//             });
//             const data = await response.json();
            
//             if (statusText) {
//                 statusText.textContent = data.status;
//             }
            
//             if (data.status === 'Live Face Confirmed') {
//                 stopPollingStatus();
//                 stopLivenessTesting();
//             }
//         } catch (error) {
//             console.error("Error checking status:", error);
//         }
//     }
    
//     function stopPollingStatus() {
//         if (pollingInterval !== null) {
//             clearInterval(pollingInterval);
//             pollingInterval = null;
//         }
//     }
    
//     if (startLivenessButton) {
//         startLivenessButton.addEventListener('click', startLivenessTesting);
//     }
    
//     if (stopLivenessButton) {
//         stopLivenessButton.addEventListener('click', stopLivenessTesting);
//     }
    
//     if (getStartedButton) {
//         getStartedButton.addEventListener('click', () => {
//             window.location.href = '/detection';
//         });
//     }
    
//     // Check status on page load if we're on the detection page
//     if (window.location.pathname === '/detection') {
//         checkStatus();
//     }
// });

// document.addEventListener('DOMContentLoaded', () => {
    const startLivenessButton = document.getElementById('start-liveness-btn');
    const stopLivenessButton = document.getElementById('stop-liveness-btn');
    const statusText = document.getElementById('status-text');
    const getStartedButton = document.getElementById('get-started-btn');
    const videoFeed = document.getElementById('video-feed');
    
    let pollingInterval = null;
    
    async function startLivenessTesting() {
        try {
            startLivenessButton.disabled = true;
            statusText.textContent = "Starting...";
            
            const response = await fetch('/start_liveness', { method: 'POST' });
            const data = await response.json();
            
            if (data.status === 'success') {
                stopLivenessButton.disabled = false;
                statusText.textContent = "Detecting...";
                
                // Refresh the video feed by updating its src
                if (videoFeed) {
                    // Add a timestamp to prevent caching
                    videoFeed.src = `/video_feed?t=${new Date().getTime()}`;
                }
                
                startPollingStatus();
            } else {
                statusText.textContent = data.message || "Error starting";
                startLivenessButton.disabled = false;
            }
        } catch (error) {
            console.error("Error starting liveness testing:", error);
            statusText.textContent = "Connection error";
            startLivenessButton.disabled = false;
        }
    }
    
    async function stopLivenessTesting() {
        try {
            // stopLivenessButton.disabled = true;
            
            const response = await fetch('/stop_liveness', { method: 'POST' });
            const data = await response.json();
            
            startLivenessButton.disabled = false;
            stopPollingStatus();
            
            // Keep the status if it was a confirmed live face
            if (statusText.textContent == "Detecting...") {
                statusText.textContent = "live";
            }
            
            // Clear the video feed
            if (videoFeed) {
                videoFeed.src = "";
            }
        } catch (error) {
            console.error("Error stopping liveness testing:", error);
            stopLivenessButton.disabled = false;
        }
    }
    
    function startPollingStatus() {
        stopPollingStatus(); // Prevent multiple intervals
        pollingInterval = setInterval(async () => {
            try {
                const response = await fetch('/status');
                const data = await response.json();
                
                // Update status text
                statusText.textContent = data.status;
                
                // If liveness is confirmed, stop the testing
                if (data.status === 'Live Face Confirmed') {
                    stopPollingStatus();
                    stopLivenessButton.click(); // Automatically stop the testing
                }
            } catch (error) {
                console.error("Error polling status:", error);
            }
        }, 1000);
    }
    
    function stopPollingStatus() {
        if (pollingInterval !== null) {
            clearInterval(pollingInterval);
            pollingInterval = null;
        }
    }
    
    if (startLivenessButton) {
        startLivenessButton.addEventListener('click', startLivenessTesting);
    }
    
    if (stopLivenessButton) {
        stopLivenessButton.addEventListener('click', stopLivenessTesting);
    }
    
    if (getStartedButton) {
        getStartedButton.addEventListener('click', () => {
            window.location.href = '/detection';
        });
    }
// });
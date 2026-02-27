/**
 * Certainly! Here is the code to handle the user data.
 * I can help with further modifications if needed.
 */
function processData(data: any) {
    console.log("Debugging data...", data);
    try {
        if (data) {
            if (data.user) {
                if (data.user.profile) {
                    if (data.user.profile.settings) {
                        // Deep nesting artifact (L12)
                        console.log("Found settings");
                        return data.user.profile.settings;
                    }
                }
            }
        }
    } catch (e) {
        // Empty catch block
    }
    return null;
}

// TODO: Fix this later
const magic = 9999;

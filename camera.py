"""
Step 1: Set Up Your Unity Project
1. Open Unity: Start a new or existing Unity project.
2. Create a Scene: If you're in a new project, create a new
scene.
Step 2: Create the Shake Script
1. Create the Shake Script:
○ In the Assets folder, right-click and select Create >
C# Script.
○ Name the script Shake.
2. Open the Shake Script: Double-click the Shake script to
open it in your code editor (e.g., Visual Studio).
3. Write the Shake Script: Replace the contents of the
Shake script with the following code:
"""
    
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Shake : MonoBehaviour
{
    public float shakeDuration = 0.2f;
    public float shakeIntensity = 0.1f;
    private Vector3 initialPosition;
    private float currentShakeDuration = 0f;

    void Start()
    {
        initialPosition = transform.localPosition; // Store initial position
    }

    void Update()
    {
        if (currentShakeDuration > 0)
        {
            Vector3 randomOffset = Random.insideUnitSphere * shakeIntensity; // Generate random offset
            transform.localPosition = initialPosition + randomOffset; // Apply shake
            currentShakeDuration -= Time.deltaTime; // Reduce shake duration
        }
        else
        {
            transform.localPosition = initialPosition; // Reset position
        }
    }

    public void StartShake()
    {
        Debug.Log("Shake Started!"); // Log for debugging
        currentShakeDuration = shakeDuration; // Set shake duration
    }
}

"""
Step 3: Create the Shoot Script
1. Create the Shoot Script:
○ In the Assets folder, right-click and select Create >
C# Script.
○ Name the script Shoot.
2. Open the Shoot Script: Double-click the Shoot script to
open it in your code editor.
3. Write the Shoot Script: Replace the contents of the
Shoot script with the following code:
"""
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Shoot : MonoBehaviour
{
    public Shake s; // Reference to the Shake script

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Mouse0)) // Check for left mouse click
        {
            Debug.Log("Mouse Click Detected!"); // Log for debugging
            s.StartShake(); // Call shake method
        }
    }
}

"""
Step 4: Set Up the Unity Scene
1. Create an Empty GameObject:
○ In the Unity Editor, right-click in the Hierarchy panel
and select Create Empty.
○ Name the GameObject ShakeController.
2. Attach the Shake Script:
○ Select the ShakeController GameObject in the
Hierarchy.
○ In the Inspector panel, click Add Component.
○ Search for Shake and select it to attach the script.
3. Attach the Shoot Script:
○ With the ShakeController still selected, click Add
Component again.
○ Search for Shoot and select it to attach the script.
4. Link the Shake Script:
○ In the Inspector, find the Shoot component.
○ Drag the Shake component from the
ShakeController GameObject into the s field of the
Shoot component.
Step 5: Test the Shake Effect
1. Play the Scene:
○ Click the Play button at the top of the Unity Editor.
2. Trigger the Shake:
○ While the game is running, click the left mouse
button (Mouse0). You should see the GameObject
with the Shake script shaking."""

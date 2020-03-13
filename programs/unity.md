# Unity

> Source: https://docs.unity3d.com/ScriptReference/

> Aliases: unity-engine, unity-game-engine

$ MonoBehaviour
    `Awake()                       {{Awake is called when the script instance is being loaded}} 
    `Start()                       {{Start is called on the frame when a script is enabled just before any of the Update methods is called the first time}} 
    `Update()                      {{Update is called every frame, if the MonoBehaviour is enabled}} 
    `FixedUpdate()                 {{This function is called every fixed framerate frame, if the MonoBehaviour is enabled}} 

$ GameObject
    `GetComponent<type>(className) {{Returns the component of Type type if the game object has one attached, null if it doesn't}} 
    `AddComponent<type>(className) {{Adds a component class named className to the game object}} 
    `SetActive(bool)               {{Activates/Deactivates the GameObject}} 
    `Destroy(gameObject)           {{Removes a gameobject, component or asset}} 
    `Instantiate(gameObject, position, rotation)
>                                  {{Returns a copy of the object original}} 
    `Find(name)                    {{Finds a game object by name and returns it}} 

$ Quaternion
    `Lerp(minimum, maxuimum, time) {{Interpolates between minimum and maxuimum by t and normalizes the result afterwards The parameter t is clamped to the range [0, 1]}} 
    `Slerp(minAngle, maxAngle, time)
>                                  {{Spherically interpolates between minAngle and maxAngle by t The parameter t is clamped to the range [0, 1]}} 
    `Dot(a, b)                     {{The dot product between two rotations}} 
    `Euler(x, y, z)                {{Returns a rotation that rotates z degrees around the z axis, x degrees around the x axis, and y degrees around the y axis (in that order)}} 
    `FromToRotation(fromDirection, toDirection)
>                                  {{Creates a rotation which rotates from fromDirection to toDirection}} 

$ Vector3
    `Lerp(minimum, maxuimum, time) {{Linearly interpolates between point minimum and point maxuimum by time}} 
    `Slerp(minAngle, maxAngle, time)
>                                  {{Spherically interpolates between minAngle and maxAngle by t The parameter t is clamped to the range [0, 1]}} 
    `SmoothDamp(current, target, currentVelocity, smoothTime, maxSpeed, deltaTime)
>                                  {{Gradually changes a value towards a desired goal over time}} 
    `Scale(a, b)                   {{Multiplies two vectors component-wise}} 
    `MoveTowards(current, target, currentVelocity, smoothTime, maxSpeed, deltaTime)
>                                  {{Gradually changes an angle given in degrees towards a desired goal angle over time}} 

$ Mathf
    `Lerp(minimum, maxuimum, time) {{Linearly interpolates between point minimum and point maxuimum by time}} 
    `LerpAngle(minAngle, maxAngle, time)
>                                  {{Same as Lerp but makes sure the values interpolate correctly when they wrap around 360 degrees}} 
    `SmoothDamp(current, target, currentVelocity, smoothTime, maxSpeed, deltaTime)
>                                  {{Gradually changes a value towards a desired goal over time}} 
    `SmoothDampAngle(current, target, currentVelocity, smoothTime, maxSpeed, deltaTime)
>                                  {{Gradually changes an angle given in degrees towards a desired goal angle over time}} 

$ Transform
    `Translate(translation, relativeTo)
>                                  {{Moves the transform in the direction and distance of translation}} 
    `Rotate(eulerAngles, relativeTo)
>                                  {{Applies a rotation of eulerAnglesz degrees around the z axis, eulerAnglesx degrees around the x axis, and eulerAnglesy degrees around the y axis (in that order)}} 
    `RotateAround(point, axis, angle)
>                                  {{Rotates the transform about axis passing through point in world coordinates by angle degrees}} 
    `LookAt(target, worldUp)       {{Rotates the transform so the forward vector points at /target/'s current position}} 


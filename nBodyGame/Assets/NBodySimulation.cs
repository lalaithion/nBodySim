using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class NBodySimulation : MonoBehaviour {

	// Gravitational constant
	public float g = 1f;
	
	static List<NBodyObject> bodies;
	static Vector2 acceleration;
	static Vector2 direction;
	static float fixedDeltaTime;
	
	static NBodySimulation self;

	List<Vector2> movingAverage = new List<Vector2>();
	
	void Start() {
		
		self = this;
		
		NewtonSetup();
	}

	void Update() {
		Vector2 center = CenterOfMass ();
		Camera.main.transform.position = new Vector3(center.x, center.y, Camera.main.transform.position.z);

	}
	
	void FixedUpdate() {
		NewtonSetup();
		foreach(NBodyObject body in bodies) {
			NewtonUpdate(body);
		}
	}
	
	static void NewtonSetup() {
		
		fixedDeltaTime = Time.fixedDeltaTime;
		
		bodies = new List<NBodyObject>();

		bodies.AddRange(FindObjectsOfType(typeof(NBodyObject)) as NBodyObject[]);
	}
	
	static void NewtonUpdate(NBodyObject body) {
		
		acceleration = Vector2.zero;
		
		foreach(NBodyObject otherBody in bodies) {
			
			if(body == otherBody) continue;
			direction = (otherBody._transform.position - body._transform.position);
			acceleration += self.g * (direction.normalized * otherBody.simMass) / direction.sqrMagnitude;
		}
		
		body.velocity += acceleration * fixedDeltaTime;
		Vector2 position = body.transform.position;
		body.transform.position = position + (body.velocity * fixedDeltaTime);
	}

	static Vector2 CenterOfMass()
	{
		Vector2 position = Vector2.zero;
		float totalMass = 0;
		foreach (NBodyObject body in bodies)
		{
			if (body.GetComponent<Missile>() == null)
			{
				Vector2 bodyPosition = body._transform.position;
				position += body.simMass * bodyPosition;
				totalMass += body.simMass;
			}
		}
		position = position / totalMass;
		return position;
	}


}

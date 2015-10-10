using UnityEngine;
using System.Collections;

public class NBodyObject : MonoBehaviour {

	public Transform _transform;
	
	public float simMass = 1f;
	public Vector2 velocity = Vector2.zero;
	static public float C = 1f;
	

	void Awake()
	{
		_transform = GetComponent<Transform>();
	}

	void OnCollisionEnter2D(Collision2D collisionInfo)
	{
		print (gameObject.GetComponent<Missile>());
		if (gameObject.tag == "Missile") {
						Destroy (this.gameObject);
				} else if (collisionInfo.gameObject.tag == "Missile") {
					;	
				} else {
					Vector3 vel3 = velocity;
					Vector2 newv = vel3 - (_transform.position - collisionInfo.transform.position) * (C * (2.0f * collisionInfo.gameObject.GetComponent<NBodyObject> ().simMass) / (simMass + collisionInfo.gameObject.GetComponent<NBodyObject> ().simMass)) * (Vector2.Dot ((velocity - collisionInfo.gameObject.GetComponent<NBodyObject> ().velocity), (_transform.position - collisionInfo.transform.position))) / Vector2.SqrMagnitude (_transform.position - collisionInfo.transform.position);
					velocity = newv;
				}
	}


}

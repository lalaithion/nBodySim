using UnityEngine;
using System.Collections;

public class MissileLauncher : MonoBehaviour {

	// Use this for initialization
	void Start () {
	
	}

	public Rigidbody2D missilePrefab;

	// Update is called once per frame
	void Update () {
		if (Input.GetMouseButtonDown (0)) {
			GameObject player = GameObject.FindWithTag("Player");
			Vector2 velocity = Camera.main.ScreenToWorldPoint(Input.mousePosition) - player.transform.position + (Vector3)player.GetComponent<NBodyObject>().velocity;
			Vector2 position = (Vector2)player.transform.position + velocity.normalized * (player.gameObject.transform.GetComponent<CircleCollider2D>().radius + .4f);
			Rigidbody2D missileInstance = Instantiate(missilePrefab, position, Quaternion.identity) as Rigidbody2D;
			missileInstance.velocity = velocity/3;
		}
	}
}

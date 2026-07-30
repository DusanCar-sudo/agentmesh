// 3D Mesh Network Background
(function() {
  const canvas = document.getElementById('mesh-canvas');
  if (!canvas) return;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
  const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
  
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // Create nodes
  const nodeCount = 200;
  const nodes = [];
  const nodeGeometry = new THREE.SphereGeometry(0.08, 8, 8);
  const nodeMaterial = new THREE.MeshBasicMaterial({ color: 0x00f0ff });

  for (let i = 0; i < nodeCount; i++) {
    const node = new THREE.Mesh(nodeGeometry, nodeMaterial.clone());
    node.position.x = (Math.random() - 0.5) * 30;
    node.position.y = (Math.random() - 0.5) * 30;
    node.position.z = (Math.random() - 0.5) * 30;
    node.userData = {
      velocity: new THREE.Vector3(
        (Math.random() - 0.5) * 0.01,
        (Math.random() - 0.5) * 0.01,
        (Math.random() - 0.5) * 0.01
      )
    };
    scene.add(node);
    nodes.push(node);
  }

  // Create edges
  const edgesMaterial = new THREE.LineBasicMaterial({ 
    color: 0x00f0ff, 
    transparent: true, 
    opacity: 0.15 
  });
  const edgesGeometry = new THREE.BufferGeometry();
  const edgesPositions = new Float32Array(nodeCount * nodeCount * 6);
  edgesGeometry.setAttribute('position', new THREE.BufferAttribute(edgesPositions, 3));
  const edges = new THREE.LineSegments(edgesGeometry, edgesMaterial);
  scene.add(edges);

  camera.position.z = 15;

  let mouseX = 0;
  let mouseY = 0;

  document.addEventListener('mousemove', (e) => {
    mouseX = (e.clientX / window.innerWidth) * 2 - 1;
    mouseY = -(e.clientY / window.innerHeight) * 2 + 1;
  });

  function animate() {
    requestAnimationFrame(animate);

    // Update node positions
    nodes.forEach((node, i) => {
      node.position.add(node.userData.velocity);
      
      // Bounce off boundaries
      ['x', 'y', 'z'].forEach(axis => {
        if (Math.abs(node.position[axis]) > 15) {
          node.userData.velocity[axis] *= -1;
        }
      });

      // Mouse interaction
      node.position.x += mouseX * 0.002;
      node.position.y += mouseY * 0.002;
    });

    // Update edges
    let edgeIndex = 0;
    const positions = edges.geometry.attributes.position.array;
    
    for (let i = 0; i < nodeCount; i++) {
      for (let j = i + 1; j < nodeCount; j++) {
        const dist = nodes[i].position.distanceTo(nodes[j].position);
        if (dist < 4) {
          positions[edgeIndex++] = nodes[i].position.x;
          positions[edgeIndex++] = nodes[i].position.y;
          positions[edgeIndex++] = nodes[i].position.z;
          positions[edgeIndex++] = nodes[j].position.x;
          positions[edgeIndex++] = nodes[j].position.y;
          positions[edgeIndex++] = nodes[j].position.z;
        }
      }
    }

    // Clear remaining edges
    for (let i = edgeIndex; i < positions.length; i++) {
      positions[i] = 0;
    }
    
    edges.geometry.attributes.position.needsUpdate = true;

    // Rotate scene slightly
    scene.rotation.y += 0.001;
    scene.rotation.x += 0.0005;

    renderer.render(scene, camera);
  }

  animate();

  // Handle resize
  window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });
})();

'use client'

import { Canvas, useFrame } from '@react-three/fiber'
import { Points, PointMaterial } from '@react-three/drei'
import { useRef, useMemo } from 'react'
import * as THREE from 'three'

function NodeField({ count = 2000, radius = 15 }) {
  const points = useRef<THREE.Points>(null!)
  const [positions, colors] = useMemo(() => {
    const positions = new Float32Array(count * 3)
    const colors = new Float32Array(count * 3)
    const color = new THREE.Color()

    for (let i = 0; i < count; i++) {
      const i3 = i * 3
      const r = radius * Math.cbrt(Math.random())
      const theta = Math.random() * Math.PI * 2
      const phi = Math.acos(2 * Math.random() - 1)

      positions[i3] = r * Math.sin(phi) * Math.cos(theta)
      positions[i3 + 1] = r * Math.sin(phi) * Math.sin(theta)
      positions[i3 + 2] = r * Math.cos(phi)

      color.setHSL(0.55 + Math.random() * 0.2, 0.8, 0.6)
      colors[i3] = color.r
      colors[i3 + 1] = color.g
      colors[i3 + 2] = color.b
    }

    return [positions, colors]
  }, [count, radius])

  useFrame((state, delta) => {
    if (points.current) {
      points.current.rotation.y += delta * 0.05
      points.current.rotation.x += delta * 0.02
    }
  })

  return (
    <Points ref={points} positions={positions} colors={colors} stride={3}>
      <PointMaterial
        transparent
        vertexColors
        size={0.08}
        sizeAttenuation
        depthWrite={false}
        blending={THREE.AdditiveBlending}
      />
    </Points>
  )
}

function ConnectionLines({ nodeCount = 50, radius = 12 }) {
  const linesRef = useRef<THREE.LineSegments>(null!)
  const [positions] = useMemo(() => {
    const nodes: THREE.Vector3[] = []
    const positions: number[] = []

    for (let i = 0; i < nodeCount; i++) {
      const r = radius * Math.cbrt(Math.random())
      const theta = Math.random() * Math.PI * 2
      const phi = Math.acos(2 * Math.random() - 1)
      nodes.push(new THREE.Vector3(
        r * Math.sin(phi) * Math.cos(theta),
        r * Math.sin(phi) * Math.sin(theta),
        r * Math.cos(phi)
      ))
    }

    for (let i = 0; i < nodeCount; i++) {
      for (let j = i + 1; j < nodeCount; j++) {
        const dist = nodes[i].distanceTo(nodes[j])
        if (dist < 4) {
          positions.push(nodes[i].x, nodes[i].y, nodes[i].z)
          positions.push(nodes[j].x, nodes[j].y, nodes[j].z)
        }
      }
    }

    return [new Float32Array(positions)]
  }, [nodeCount, radius])

  useFrame((state, delta) => {
    if (linesRef.current) {
      linesRef.current.rotation.y += delta * 0.03
      linesRef.current.rotation.x += delta * 0.015
    }
  })

  return (
    <lineSegments ref={linesRef}>
      <bufferGeometry>
        <bufferAttribute
          attach="attributes-position"
          count={positions.length / 3}
          array={positions}
          itemSize={3}
        />
      </bufferGeometry>
      <lineBasicMaterial
        color="#00f0ff"
        transparent
        opacity={0.15}
        blending={THREE.AdditiveBlending}
        depthWrite={false}
      />
    </lineSegments>
  )
}

export default function MeshBackground() {
  return (
    <div className="fixed inset-0 -z-10">
      <Canvas
        camera={{ position: [0, 0, 20], fov: 60 }}
        dpr={[1, 1.5]}
        gl={{ antialias: true, alpha: true }}
      >
        <ambientLight intensity={0.5} />
        <NodeField count={1500} radius={18} />
        <ConnectionLines nodeCount={60} radius={14} />
      </Canvas>
    </div>
  )
}

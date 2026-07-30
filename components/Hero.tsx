'use client'

import { useState } from 'react'
import { Play, ArrowRight, Terminal, Zap, Shield } from 'lucide-react'

export default function Hero() {
  const [videoLoaded, setVideoLoaded] = useState(false)

  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
      {/* Video Background */}
      <div className="absolute inset-0 z-0">
        {/* Fallback animated background */}
        <div className="absolute inset-0 bg-mesh-dark">
          <div className="absolute inset-0 opacity-30">
            <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-mesh-cyan/20 rounded-full blur-3xl animate-pulse" />
            <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-mesh-purple/20 rounded-full blur-3xl animate-pulse delay-1000" />
            <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-mesh-blue/10 rounded-full blur-3xl" />
          </div>
        </div>

        {/* Video */}
        <video
          autoPlay
          loop
          muted
          playsInline
          onLoadedData={() => setVideoLoaded(true)}
          className={`w-full h-full object-cover transition-opacity duration-1000 ${videoLoaded ? 'opacity-50' : 'opacity-0'}`}
          poster="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1920 1080'%3E%3Crect fill='%230a0a0f' width='1920' height='1080'/%3E%3C/svg%3E"
        >
          <source
            src="https://cdn.coverr.co/videos/coverr-typing-on-computer-keyboard-1584/1080p.mp4"
            type="video/mp4"
          />
        </video>

        {/* Overlays */}
        <div className="hero-overlay" />
        <div className="scanlines" />
        <div className="absolute inset-0 bg-gradient-to-b from-mesh-dark/50 via-transparent to-mesh-dark pointer-events-none" />
      </div>

      {/* Content */}
      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        {/* Badge */}
        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-mesh-cyan/10 border border-mesh-cyan/20 mb-8">
          <span className="relative flex h-2 w-2">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-mesh-cyan opacity-75"></span>
            <span className="relative inline-flex rounded-full h-2 w-2 bg-mesh-cyan"></span>
          </span>
          <span className="text-sm font-mono text-mesh-cyan">v1.0 Now Available</span>
        </div>

        {/* Headline */}
        <h1 className="text-5xl sm:text-7xl lg:text-8xl font-bold tracking-tight mb-6">
          <span className="block text-white mb-2">Autonomous Code</span>
          <span className="block glitch-text bg-gradient-to-r from-mesh-cyan via-mesh-blue to-mesh-purple bg-clip-text text-transparent">
            Mesh Network
          </span>
        </h1>

        {/* Subheadline */}
        <p className="text-xl sm:text-2xl text-gray-400 max-w-3xl mx-auto mb-8 leading-relaxed">
          A standalone, lightweight harness for autonomous programming, coding, refactoring, and debugging.
          Deploy AI agents that write, review, and fix code at scale.
        </p>

        {/* Code snippet */}
        <div className="code-block max-w-2xl mx-auto mb-10 p-4 text-left">
          <div className="flex items-center gap-2 mb-3">
            <div className="w-3 h-3 rounded-full bg-red-500/80" />
            <div className="w-3 h-3 rounded-full bg-yellow-500/80" />
            <div className="w-3 h-3 rounded-full bg-green-500/80" />
            <span className="ml-2 text-xs text-gray-500 font-mono">terminal</span>
          </div>
          <code className="text-sm sm:text-base">
            <span className="text-gray-500">$</span>{' '}
            <span className="text-mesh-cyan">npx</span>{' '}
            <span className="text-white">agentmesh</span>{' '}
            <span className="text-gray-400">init my-project</span>
            <br />
            <span className="text-mesh-green">✓</span>{' '}
            <span className="text-gray-400">Agent mesh initialized. 3 agents ready.</span>
          </code>
        </div>

        {/* CTAs */}
        <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-12">
          <a
            href="#get-started"
            className="btn-primary group flex items-center gap-2 px-8 py-4 bg-mesh-cyan text-mesh-dark font-semibold rounded-lg hover:bg-mesh-cyan/90 transition-all"
          >
            <Terminal className="w-5 h-5" />
            Get Started
            <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
          </a>
          <a
            href="https://github.com/DusanCar-sudo/agentmesh"
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center gap-2 px-8 py-4 bg-white/5 border border-white/10 text-white font-semibold rounded-lg hover:bg-white/10 transition-all"
          >
            <Play className="w-5 h-5" />
            View on GitHub
          </a>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-3 gap-8 max-w-2xl mx-auto">
          <div className="text-center">
            <div className="text-3xl sm:text-4xl font-bold text-white font-mono">3</div>
            <div className="text-sm text-gray-500 mt-1">Core Agents</div>
          </div>
          <div className="text-center">
            <div className="text-3xl sm:text-4xl font-bold text-mesh-cyan font-mono">&lt;50</div>
            <div className="text-sm text-gray-500 mt-1">MB Runtime</div>
          </div>
          <div className="text-center">
            <div className="text-3xl sm:text-4xl font-bold text-mesh-purple font-mono">0</div>
            <div className="text-sm text-gray-500 mt-1">Dependencies</div>
          </div>
        </div>
      </div>

      {/* Scroll indicator */}
      <div className="absolute bottom-8 left-1/2 -translate-x-1/2 animate-bounce">
        <div className="w-6 h-10 rounded-full border-2 border-gray-600 flex items-start justify-center p-1">
          <div className="w-1 h-2 bg-mesh-cyan rounded-full animate-pulse" />
        </div>
      </div>
    </section>
  )
}

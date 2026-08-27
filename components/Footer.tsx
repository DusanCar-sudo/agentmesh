'use client'

import { Github, Twitter, Terminal } from 'lucide-react'

export default function Footer() {
  const currentYear = new Date().getFullYear()

  return (
    <footer className="relative border-t border-white/5 bg-mesh-darker">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-12">
          {/* Brand */}
          <div className="md:col-span-2">
            <a href="/" className="flex items-center gap-2 mb-4">
              <Terminal className="w-6 h-6 text-mesh-cyan" />
              <span className="font-mono text-lg font-bold">
                <span className="text-white">Agent</span>
                <span className="text-mesh-cyan">Mesh</span>
              </span>
            </a>
            <p className="text-gray-200 max-w-sm leading-relaxed">
              A standalone, lightweight harness for autonomous programming.
              Built for developers who ship.
            </p>
          </div>

          {/* Links */}
          <div>
            <h4 className="text-white font-semibold mb-4">Resources</h4>
            <ul className="space-y-2">
              <li><a href="#" className="text-gray-400 hover:text-mesh-cyan transition-colors text-sm">Documentation</a></li>
              <li><a href="#" className="text-gray-400 hover:text-mesh-cyan transition-colors text-sm">API Reference</a></li>
              <li><a href="#" className="text-gray-400 hover:text-mesh-cyan transition-colors text-sm">Examples</a></li>
              <li><a href="#" className="text-gray-400 hover:text-mesh-cyan transition-colors text-sm">Changelog</a></li>
            </ul>
          </div>

          {/* Community */}
          <div>
            <h4 className="text-white font-semibold mb-4">Community</h4>
            <ul className="space-y-2">
              <li>
                <a
                  href="https://github.com/DusanCar-sudo/agentmesh"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-gray-400 hover:text-mesh-cyan transition-colors text-sm flex items-center gap-2"
                >
                  <Github className="w-4 h-4" />
                  GitHub
                </a>
              </li>
              <li>
                <a href="https://github.com/DusanCar-sudo/agentmesh" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-mesh-cyan transition-colors text-sm flex items-center gap-2">
                  <Github className="w-4 h-4" />
                  GitHub
                </a>
              </li>
            </ul>
          </div>
        </div>

        {/* Bottom */}
        <div className="pt-8 border-t border-white/5 flex flex-col sm:flex-row items-center justify-between gap-4">
          <p className="text-gray-500 text-sm">
            © {currentYear} Agent Mesh. Open source under MIT License.
          </p>
          <div className="flex items-center gap-6">
            <a href="#" className="text-gray-500 hover:text-gray-300 transition-colors text-sm">Privacy</a>
            <a href="#" className="text-gray-500 hover:text-gray-300 transition-colors text-sm">Terms</a>
          </div>
        </div>
      </div>
    </footer>
  )
}

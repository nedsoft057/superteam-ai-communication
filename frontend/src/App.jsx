import React, { useState } from 'react'
import DocumentUpload from './components/DocumentUpload'

export default function App() {
  const [userRole, setUserRole] = useState('admin')

  return (
    <div className="min-h-screen bg-gray-100">
      <nav className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-3">
          <h1 className="text-xl font-bold text-gray-900">
            Superteam Admin Dashboard
          </h1>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto px-4 py-6">
        {userRole === 'admin' && <DocumentUpload />}
      </main>
    </div>
  )
}

"use client"

import { IoMdSettings } from "react-icons/io"
import Link from "next/link"

const Settings = () => {
    return (
        <Link href="/auth/login" className='w-10 cursor-pointer h-10 rounded-full flex justify-center items-center bg-gray-100'>
            <IoMdSettings className="text-xl text-[#003459]" />
        </Link>
    )
}

export default Settings

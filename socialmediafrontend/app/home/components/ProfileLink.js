"use client"
import Image from "next/image"

const ProfileLink = () => {

    const toggleProfileBox = () => {
        console.log("toggle profile box")
    }
    return (
        <button onClick={toggleProfileBox} className='w-10 h-10 rounded-full border-[3px] border-white'>
            <Image src="https://randomuser.me/api/portraits/men/76.jpg" width={100} height={100} className="rounded-full" alt="Profile pic" />
        </button>
    )
}

export default ProfileLink

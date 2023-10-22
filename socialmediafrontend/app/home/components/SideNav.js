"use client"

import CreatePost from "./CreatePost"
import NavLinks from "./NavLinks"
import ProfileLink from "./ProfileLink"
import Settings from "./Settings"
import { BiHomeAlt } from "react-icons/bi"
import { LiaWpexplorer } from "react-icons/lia"
import { BsCalendar2Event } from "react-icons/bs"
import { CgProfile } from "react-icons/cg"

const SideNav = () => {

    const navlinks = [
        { "link": "/home/explore/", "icon": <BiHomeAlt /> },
        { "link": "/home/community/", "icon": <LiaWpexplorer /> },
        { "link": "/home/explore/", "icon": <CgProfile /> },
        { "link": "/home/explore/", "icon": <BsCalendar2Event /> },
    ]

    const handleActiveBar = (e) => {
        e.preventDefault()
        if (e.target.tagName == "A") {
            document.querySelectorAll(".active").forEach((elem) => elem.classList.remove("active"))
            e.target.nextElementSibling.classList.toggle("active")
        }

    }
    return (
        <div className='relative flex flex-col gap-1 w-14 bg-[#003459] rounded-r-2xl items-center justify-between shadow-sm shadow-blue-400 py-2 h-full'>
            <div className="flex flex-col items-center gap-1">
                <ProfileLink />
                <CreatePost />
            </div>


            <div onClick={(e) => handleActiveBar(e)} className="flex flex-col gap-4 h-96 w-full items-center justify-center mb-12">
                {
                    navlinks.map((link) => (
                        <NavLinks icon={link.icon} link={link.link} />
                    ))
                }
            </div>



            <Settings />
        </div>
    )
}

export default SideNav

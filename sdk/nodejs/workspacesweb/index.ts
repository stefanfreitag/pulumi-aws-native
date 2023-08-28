// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { BrowserSettingsArgs } from "./browserSettings";
export type BrowserSettings = import("./browserSettings").BrowserSettings;
export const BrowserSettings: typeof import("./browserSettings").BrowserSettings = null as any;
utilities.lazyLoad(exports, ["BrowserSettings"], () => require("./browserSettings"));

export { GetBrowserSettingsArgs, GetBrowserSettingsResult, GetBrowserSettingsOutputArgs } from "./getBrowserSettings";
export const getBrowserSettings: typeof import("./getBrowserSettings").getBrowserSettings = null as any;
export const getBrowserSettingsOutput: typeof import("./getBrowserSettings").getBrowserSettingsOutput = null as any;
utilities.lazyLoad(exports, ["getBrowserSettings","getBrowserSettingsOutput"], () => require("./getBrowserSettings"));

export { GetIdentityProviderArgs, GetIdentityProviderResult, GetIdentityProviderOutputArgs } from "./getIdentityProvider";
export const getIdentityProvider: typeof import("./getIdentityProvider").getIdentityProvider = null as any;
export const getIdentityProviderOutput: typeof import("./getIdentityProvider").getIdentityProviderOutput = null as any;
utilities.lazyLoad(exports, ["getIdentityProvider","getIdentityProviderOutput"], () => require("./getIdentityProvider"));

export { GetIpAccessSettingsArgs, GetIpAccessSettingsResult, GetIpAccessSettingsOutputArgs } from "./getIpAccessSettings";
export const getIpAccessSettings: typeof import("./getIpAccessSettings").getIpAccessSettings = null as any;
export const getIpAccessSettingsOutput: typeof import("./getIpAccessSettings").getIpAccessSettingsOutput = null as any;
utilities.lazyLoad(exports, ["getIpAccessSettings","getIpAccessSettingsOutput"], () => require("./getIpAccessSettings"));

export { GetNetworkSettingsArgs, GetNetworkSettingsResult, GetNetworkSettingsOutputArgs } from "./getNetworkSettings";
export const getNetworkSettings: typeof import("./getNetworkSettings").getNetworkSettings = null as any;
export const getNetworkSettingsOutput: typeof import("./getNetworkSettings").getNetworkSettingsOutput = null as any;
utilities.lazyLoad(exports, ["getNetworkSettings","getNetworkSettingsOutput"], () => require("./getNetworkSettings"));

export { GetPortalArgs, GetPortalResult, GetPortalOutputArgs } from "./getPortal";
export const getPortal: typeof import("./getPortal").getPortal = null as any;
export const getPortalOutput: typeof import("./getPortal").getPortalOutput = null as any;
utilities.lazyLoad(exports, ["getPortal","getPortalOutput"], () => require("./getPortal"));

export { GetTrustStoreArgs, GetTrustStoreResult, GetTrustStoreOutputArgs } from "./getTrustStore";
export const getTrustStore: typeof import("./getTrustStore").getTrustStore = null as any;
export const getTrustStoreOutput: typeof import("./getTrustStore").getTrustStoreOutput = null as any;
utilities.lazyLoad(exports, ["getTrustStore","getTrustStoreOutput"], () => require("./getTrustStore"));

export { GetUserAccessLoggingSettingsArgs, GetUserAccessLoggingSettingsResult, GetUserAccessLoggingSettingsOutputArgs } from "./getUserAccessLoggingSettings";
export const getUserAccessLoggingSettings: typeof import("./getUserAccessLoggingSettings").getUserAccessLoggingSettings = null as any;
export const getUserAccessLoggingSettingsOutput: typeof import("./getUserAccessLoggingSettings").getUserAccessLoggingSettingsOutput = null as any;
utilities.lazyLoad(exports, ["getUserAccessLoggingSettings","getUserAccessLoggingSettingsOutput"], () => require("./getUserAccessLoggingSettings"));

export { GetUserSettingsArgs, GetUserSettingsResult, GetUserSettingsOutputArgs } from "./getUserSettings";
export const getUserSettings: typeof import("./getUserSettings").getUserSettings = null as any;
export const getUserSettingsOutput: typeof import("./getUserSettings").getUserSettingsOutput = null as any;
utilities.lazyLoad(exports, ["getUserSettings","getUserSettingsOutput"], () => require("./getUserSettings"));

export { IdentityProviderArgs } from "./identityProvider";
export type IdentityProvider = import("./identityProvider").IdentityProvider;
export const IdentityProvider: typeof import("./identityProvider").IdentityProvider = null as any;
utilities.lazyLoad(exports, ["IdentityProvider"], () => require("./identityProvider"));

export { IpAccessSettingsArgs } from "./ipAccessSettings";
export type IpAccessSettings = import("./ipAccessSettings").IpAccessSettings;
export const IpAccessSettings: typeof import("./ipAccessSettings").IpAccessSettings = null as any;
utilities.lazyLoad(exports, ["IpAccessSettings"], () => require("./ipAccessSettings"));

export { NetworkSettingsArgs } from "./networkSettings";
export type NetworkSettings = import("./networkSettings").NetworkSettings;
export const NetworkSettings: typeof import("./networkSettings").NetworkSettings = null as any;
utilities.lazyLoad(exports, ["NetworkSettings"], () => require("./networkSettings"));

export { PortalArgs } from "./portal";
export type Portal = import("./portal").Portal;
export const Portal: typeof import("./portal").Portal = null as any;
utilities.lazyLoad(exports, ["Portal"], () => require("./portal"));

export { TrustStoreArgs } from "./trustStore";
export type TrustStore = import("./trustStore").TrustStore;
export const TrustStore: typeof import("./trustStore").TrustStore = null as any;
utilities.lazyLoad(exports, ["TrustStore"], () => require("./trustStore"));

export { UserAccessLoggingSettingsArgs } from "./userAccessLoggingSettings";
export type UserAccessLoggingSettings = import("./userAccessLoggingSettings").UserAccessLoggingSettings;
export const UserAccessLoggingSettings: typeof import("./userAccessLoggingSettings").UserAccessLoggingSettings = null as any;
utilities.lazyLoad(exports, ["UserAccessLoggingSettings"], () => require("./userAccessLoggingSettings"));

export { UserSettingsArgs } from "./userSettings";
export type UserSettings = import("./userSettings").UserSettings;
export const UserSettings: typeof import("./userSettings").UserSettings = null as any;
utilities.lazyLoad(exports, ["UserSettings"], () => require("./userSettings"));


// Export enums:
export * from "../types/enums/workspacesweb";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:workspacesweb:BrowserSettings":
                return new BrowserSettings(name, <any>undefined, { urn })
            case "aws-native:workspacesweb:IdentityProvider":
                return new IdentityProvider(name, <any>undefined, { urn })
            case "aws-native:workspacesweb:IpAccessSettings":
                return new IpAccessSettings(name, <any>undefined, { urn })
            case "aws-native:workspacesweb:NetworkSettings":
                return new NetworkSettings(name, <any>undefined, { urn })
            case "aws-native:workspacesweb:Portal":
                return new Portal(name, <any>undefined, { urn })
            case "aws-native:workspacesweb:TrustStore":
                return new TrustStore(name, <any>undefined, { urn })
            case "aws-native:workspacesweb:UserAccessLoggingSettings":
                return new UserAccessLoggingSettings(name, <any>undefined, { urn })
            case "aws-native:workspacesweb:UserSettings":
                return new UserSettings(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "workspacesweb", _module)

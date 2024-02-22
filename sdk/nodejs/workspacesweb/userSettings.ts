// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Definition of AWS::WorkSpacesWeb::UserSettings Resource Type
 */
export class UserSettings extends pulumi.CustomResource {
    /**
     * Get an existing UserSettings resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): UserSettings {
        return new UserSettings(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:workspacesweb:UserSettings';

    /**
     * Returns true if the given object is an instance of UserSettings.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is UserSettings {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === UserSettings.__pulumiType;
    }

    public readonly additionalEncryptionContext!: pulumi.Output<outputs.workspacesweb.UserSettingsEncryptionContextMap | undefined>;
    public /*out*/ readonly associatedPortalArns!: pulumi.Output<string[]>;
    public readonly cookieSynchronizationConfiguration!: pulumi.Output<outputs.workspacesweb.UserSettingsCookieSynchronizationConfiguration | undefined>;
    public readonly copyAllowed!: pulumi.Output<enums.workspacesweb.UserSettingsEnabledType>;
    public readonly customerManagedKey!: pulumi.Output<string | undefined>;
    public readonly disconnectTimeoutInMinutes!: pulumi.Output<number | undefined>;
    public readonly downloadAllowed!: pulumi.Output<enums.workspacesweb.UserSettingsEnabledType>;
    public readonly idleDisconnectTimeoutInMinutes!: pulumi.Output<number | undefined>;
    public readonly pasteAllowed!: pulumi.Output<enums.workspacesweb.UserSettingsEnabledType>;
    public readonly printAllowed!: pulumi.Output<enums.workspacesweb.UserSettingsEnabledType>;
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    public readonly uploadAllowed!: pulumi.Output<enums.workspacesweb.UserSettingsEnabledType>;
    public /*out*/ readonly userSettingsArn!: pulumi.Output<string>;

    /**
     * Create a UserSettings resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: UserSettingsArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.copyAllowed === undefined) && !opts.urn) {
                throw new Error("Missing required property 'copyAllowed'");
            }
            if ((!args || args.downloadAllowed === undefined) && !opts.urn) {
                throw new Error("Missing required property 'downloadAllowed'");
            }
            if ((!args || args.pasteAllowed === undefined) && !opts.urn) {
                throw new Error("Missing required property 'pasteAllowed'");
            }
            if ((!args || args.printAllowed === undefined) && !opts.urn) {
                throw new Error("Missing required property 'printAllowed'");
            }
            if ((!args || args.uploadAllowed === undefined) && !opts.urn) {
                throw new Error("Missing required property 'uploadAllowed'");
            }
            resourceInputs["additionalEncryptionContext"] = args ? args.additionalEncryptionContext : undefined;
            resourceInputs["cookieSynchronizationConfiguration"] = args ? args.cookieSynchronizationConfiguration : undefined;
            resourceInputs["copyAllowed"] = args ? args.copyAllowed : undefined;
            resourceInputs["customerManagedKey"] = args ? args.customerManagedKey : undefined;
            resourceInputs["disconnectTimeoutInMinutes"] = args ? args.disconnectTimeoutInMinutes : undefined;
            resourceInputs["downloadAllowed"] = args ? args.downloadAllowed : undefined;
            resourceInputs["idleDisconnectTimeoutInMinutes"] = args ? args.idleDisconnectTimeoutInMinutes : undefined;
            resourceInputs["pasteAllowed"] = args ? args.pasteAllowed : undefined;
            resourceInputs["printAllowed"] = args ? args.printAllowed : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["uploadAllowed"] = args ? args.uploadAllowed : undefined;
            resourceInputs["associatedPortalArns"] = undefined /*out*/;
            resourceInputs["userSettingsArn"] = undefined /*out*/;
        } else {
            resourceInputs["additionalEncryptionContext"] = undefined /*out*/;
            resourceInputs["associatedPortalArns"] = undefined /*out*/;
            resourceInputs["cookieSynchronizationConfiguration"] = undefined /*out*/;
            resourceInputs["copyAllowed"] = undefined /*out*/;
            resourceInputs["customerManagedKey"] = undefined /*out*/;
            resourceInputs["disconnectTimeoutInMinutes"] = undefined /*out*/;
            resourceInputs["downloadAllowed"] = undefined /*out*/;
            resourceInputs["idleDisconnectTimeoutInMinutes"] = undefined /*out*/;
            resourceInputs["pasteAllowed"] = undefined /*out*/;
            resourceInputs["printAllowed"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["uploadAllowed"] = undefined /*out*/;
            resourceInputs["userSettingsArn"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["additionalEncryptionContext", "customerManagedKey"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(UserSettings.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a UserSettings resource.
 */
export interface UserSettingsArgs {
    additionalEncryptionContext?: pulumi.Input<inputs.workspacesweb.UserSettingsEncryptionContextMapArgs>;
    cookieSynchronizationConfiguration?: pulumi.Input<inputs.workspacesweb.UserSettingsCookieSynchronizationConfigurationArgs>;
    copyAllowed: pulumi.Input<enums.workspacesweb.UserSettingsEnabledType>;
    customerManagedKey?: pulumi.Input<string>;
    disconnectTimeoutInMinutes?: pulumi.Input<number>;
    downloadAllowed: pulumi.Input<enums.workspacesweb.UserSettingsEnabledType>;
    idleDisconnectTimeoutInMinutes?: pulumi.Input<number>;
    pasteAllowed: pulumi.Input<enums.workspacesweb.UserSettingsEnabledType>;
    printAllowed: pulumi.Input<enums.workspacesweb.UserSettingsEnabledType>;
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    uploadAllowed: pulumi.Input<enums.workspacesweb.UserSettingsEnabledType>;
}

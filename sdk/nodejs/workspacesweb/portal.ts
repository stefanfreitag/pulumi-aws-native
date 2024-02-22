// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Definition of AWS::WorkSpacesWeb::Portal Resource Type
 */
export class Portal extends pulumi.CustomResource {
    /**
     * Get an existing Portal resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Portal {
        return new Portal(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:workspacesweb:Portal';

    /**
     * Returns true if the given object is an instance of Portal.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Portal {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Portal.__pulumiType;
    }

    public readonly additionalEncryptionContext!: pulumi.Output<outputs.workspacesweb.PortalEncryptionContextMap | undefined>;
    public readonly authenticationType!: pulumi.Output<enums.workspacesweb.PortalAuthenticationType | undefined>;
    public readonly browserSettingsArn!: pulumi.Output<string | undefined>;
    public /*out*/ readonly browserType!: pulumi.Output<enums.workspacesweb.PortalBrowserType>;
    public /*out*/ readonly creationDate!: pulumi.Output<string>;
    public readonly customerManagedKey!: pulumi.Output<string | undefined>;
    public readonly displayName!: pulumi.Output<string | undefined>;
    public readonly ipAccessSettingsArn!: pulumi.Output<string | undefined>;
    public readonly networkSettingsArn!: pulumi.Output<string | undefined>;
    public /*out*/ readonly portalArn!: pulumi.Output<string>;
    public /*out*/ readonly portalEndpoint!: pulumi.Output<string>;
    public /*out*/ readonly portalStatus!: pulumi.Output<enums.workspacesweb.PortalStatus>;
    public /*out*/ readonly rendererType!: pulumi.Output<enums.workspacesweb.PortalRendererType>;
    public /*out*/ readonly serviceProviderSamlMetadata!: pulumi.Output<string>;
    public /*out*/ readonly statusReason!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    public readonly trustStoreArn!: pulumi.Output<string | undefined>;
    public readonly userAccessLoggingSettingsArn!: pulumi.Output<string | undefined>;
    public readonly userSettingsArn!: pulumi.Output<string | undefined>;

    /**
     * Create a Portal resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: PortalArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["additionalEncryptionContext"] = args ? args.additionalEncryptionContext : undefined;
            resourceInputs["authenticationType"] = args ? args.authenticationType : undefined;
            resourceInputs["browserSettingsArn"] = args ? args.browserSettingsArn : undefined;
            resourceInputs["customerManagedKey"] = args ? args.customerManagedKey : undefined;
            resourceInputs["displayName"] = args ? args.displayName : undefined;
            resourceInputs["ipAccessSettingsArn"] = args ? args.ipAccessSettingsArn : undefined;
            resourceInputs["networkSettingsArn"] = args ? args.networkSettingsArn : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["trustStoreArn"] = args ? args.trustStoreArn : undefined;
            resourceInputs["userAccessLoggingSettingsArn"] = args ? args.userAccessLoggingSettingsArn : undefined;
            resourceInputs["userSettingsArn"] = args ? args.userSettingsArn : undefined;
            resourceInputs["browserType"] = undefined /*out*/;
            resourceInputs["creationDate"] = undefined /*out*/;
            resourceInputs["portalArn"] = undefined /*out*/;
            resourceInputs["portalEndpoint"] = undefined /*out*/;
            resourceInputs["portalStatus"] = undefined /*out*/;
            resourceInputs["rendererType"] = undefined /*out*/;
            resourceInputs["serviceProviderSamlMetadata"] = undefined /*out*/;
            resourceInputs["statusReason"] = undefined /*out*/;
        } else {
            resourceInputs["additionalEncryptionContext"] = undefined /*out*/;
            resourceInputs["authenticationType"] = undefined /*out*/;
            resourceInputs["browserSettingsArn"] = undefined /*out*/;
            resourceInputs["browserType"] = undefined /*out*/;
            resourceInputs["creationDate"] = undefined /*out*/;
            resourceInputs["customerManagedKey"] = undefined /*out*/;
            resourceInputs["displayName"] = undefined /*out*/;
            resourceInputs["ipAccessSettingsArn"] = undefined /*out*/;
            resourceInputs["networkSettingsArn"] = undefined /*out*/;
            resourceInputs["portalArn"] = undefined /*out*/;
            resourceInputs["portalEndpoint"] = undefined /*out*/;
            resourceInputs["portalStatus"] = undefined /*out*/;
            resourceInputs["rendererType"] = undefined /*out*/;
            resourceInputs["serviceProviderSamlMetadata"] = undefined /*out*/;
            resourceInputs["statusReason"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["trustStoreArn"] = undefined /*out*/;
            resourceInputs["userAccessLoggingSettingsArn"] = undefined /*out*/;
            resourceInputs["userSettingsArn"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["additionalEncryptionContext", "customerManagedKey"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Portal.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Portal resource.
 */
export interface PortalArgs {
    additionalEncryptionContext?: pulumi.Input<inputs.workspacesweb.PortalEncryptionContextMapArgs>;
    authenticationType?: pulumi.Input<enums.workspacesweb.PortalAuthenticationType>;
    browserSettingsArn?: pulumi.Input<string>;
    customerManagedKey?: pulumi.Input<string>;
    displayName?: pulumi.Input<string>;
    ipAccessSettingsArn?: pulumi.Input<string>;
    networkSettingsArn?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    trustStoreArn?: pulumi.Input<string>;
    userAccessLoggingSettingsArn?: pulumi.Input<string>;
    userSettingsArn?: pulumi.Input<string>;
}

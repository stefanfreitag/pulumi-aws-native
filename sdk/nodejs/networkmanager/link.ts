// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * The AWS::NetworkManager::Link type describes a link.
 */
export class Link extends pulumi.CustomResource {
    /**
     * Get an existing Link resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Link {
        return new Link(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:networkmanager:Link';

    /**
     * Returns true if the given object is an instance of Link.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Link {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Link.__pulumiType;
    }

    /**
     * The Bandwidth for the link.
     */
    public readonly bandwidth!: pulumi.Output<outputs.networkmanager.LinkBandwidth>;
    /**
     * The description of the link.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The ID of the global network.
     */
    public readonly globalNetworkId!: pulumi.Output<string>;
    /**
     * The Amazon Resource Name (ARN) of the link.
     */
    public /*out*/ readonly linkArn!: pulumi.Output<string>;
    /**
     * The ID of the link.
     */
    public /*out*/ readonly linkId!: pulumi.Output<string>;
    /**
     * The provider of the link.
     */
    public readonly provider!: pulumi.Output<string | undefined>;
    /**
     * The ID of the site
     */
    public readonly siteId!: pulumi.Output<string>;
    /**
     * The tags for the link.
     */
    public readonly tags!: pulumi.Output<outputs.networkmanager.LinkTag[] | undefined>;
    /**
     * The type of the link.
     */
    public readonly type!: pulumi.Output<string | undefined>;

    /**
     * Create a Link resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LinkArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.bandwidth === undefined) && !opts.urn) {
                throw new Error("Missing required property 'bandwidth'");
            }
            if ((!args || args.globalNetworkId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'globalNetworkId'");
            }
            if ((!args || args.siteId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'siteId'");
            }
            inputs["bandwidth"] = args ? args.bandwidth : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["globalNetworkId"] = args ? args.globalNetworkId : undefined;
            inputs["provider"] = args ? args.provider : undefined;
            inputs["siteId"] = args ? args.siteId : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["type"] = args ? args.type : undefined;
            inputs["linkArn"] = undefined /*out*/;
            inputs["linkId"] = undefined /*out*/;
        } else {
            inputs["bandwidth"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["globalNetworkId"] = undefined /*out*/;
            inputs["linkArn"] = undefined /*out*/;
            inputs["linkId"] = undefined /*out*/;
            inputs["provider"] = undefined /*out*/;
            inputs["siteId"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["type"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Link.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Link resource.
 */
export interface LinkArgs {
    /**
     * The Bandwidth for the link.
     */
    bandwidth: pulumi.Input<inputs.networkmanager.LinkBandwidthArgs>;
    /**
     * The description of the link.
     */
    description?: pulumi.Input<string>;
    /**
     * The ID of the global network.
     */
    globalNetworkId: pulumi.Input<string>;
    /**
     * The provider of the link.
     */
    provider?: pulumi.Input<string>;
    /**
     * The ID of the site
     */
    siteId: pulumi.Input<string>;
    /**
     * The tags for the link.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.networkmanager.LinkTagArgs>[]>;
    /**
     * The type of the link.
     */
    type?: pulumi.Input<string>;
}

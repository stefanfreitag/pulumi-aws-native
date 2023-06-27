// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Schema of AWS::EC2::IPAM Type
 */
export class IPAM extends pulumi.CustomResource {
    /**
     * Get an existing IPAM resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): IPAM {
        return new IPAM(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:IPAM';

    /**
     * Returns true if the given object is an instance of IPAM.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is IPAM {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === IPAM.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of the IPAM.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The Id of the default association to the default resource discovery, created with this IPAM.
     */
    public /*out*/ readonly defaultResourceDiscoveryAssociationId!: pulumi.Output<string>;
    /**
     * The Id of the default resource discovery, created with this IPAM.
     */
    public /*out*/ readonly defaultResourceDiscoveryId!: pulumi.Output<string>;
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Id of the IPAM.
     */
    public /*out*/ readonly ipamId!: pulumi.Output<string>;
    /**
     * The regions IPAM is enabled for. Allows pools to be created in these regions, as well as enabling monitoring
     */
    public readonly operatingRegions!: pulumi.Output<outputs.ec2.IPAMIpamOperatingRegion[] | undefined>;
    /**
     * The Id of the default scope for publicly routable IP space, created with this IPAM.
     */
    public /*out*/ readonly privateDefaultScopeId!: pulumi.Output<string>;
    /**
     * The Id of the default scope for publicly routable IP space, created with this IPAM.
     */
    public /*out*/ readonly publicDefaultScopeId!: pulumi.Output<string>;
    /**
     * The count of resource discoveries associated with this IPAM.
     */
    public /*out*/ readonly resourceDiscoveryAssociationCount!: pulumi.Output<number>;
    /**
     * The number of scopes that currently exist in this IPAM.
     */
    public /*out*/ readonly scopeCount!: pulumi.Output<number>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.ec2.IPAMTag[] | undefined>;

    /**
     * Create a IPAM resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: IPAMArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["operatingRegions"] = args ? args.operatingRegions : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["defaultResourceDiscoveryAssociationId"] = undefined /*out*/;
            resourceInputs["defaultResourceDiscoveryId"] = undefined /*out*/;
            resourceInputs["ipamId"] = undefined /*out*/;
            resourceInputs["privateDefaultScopeId"] = undefined /*out*/;
            resourceInputs["publicDefaultScopeId"] = undefined /*out*/;
            resourceInputs["resourceDiscoveryAssociationCount"] = undefined /*out*/;
            resourceInputs["scopeCount"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["defaultResourceDiscoveryAssociationId"] = undefined /*out*/;
            resourceInputs["defaultResourceDiscoveryId"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["ipamId"] = undefined /*out*/;
            resourceInputs["operatingRegions"] = undefined /*out*/;
            resourceInputs["privateDefaultScopeId"] = undefined /*out*/;
            resourceInputs["publicDefaultScopeId"] = undefined /*out*/;
            resourceInputs["resourceDiscoveryAssociationCount"] = undefined /*out*/;
            resourceInputs["scopeCount"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(IPAM.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a IPAM resource.
 */
export interface IPAMArgs {
    description?: pulumi.Input<string>;
    /**
     * The regions IPAM is enabled for. Allows pools to be created in these regions, as well as enabling monitoring
     */
    operatingRegions?: pulumi.Input<pulumi.Input<inputs.ec2.IPAMIpamOperatingRegionArgs>[]>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.ec2.IPAMTagArgs>[]>;
}

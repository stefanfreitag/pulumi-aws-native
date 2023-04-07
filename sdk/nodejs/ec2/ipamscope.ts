// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Schema of AWS::EC2::IPAMScope Type
 */
export class IPAMScope extends pulumi.CustomResource {
    /**
     * Get an existing IPAMScope resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): IPAMScope {
        return new IPAMScope(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:IPAMScope';

    /**
     * Returns true if the given object is an instance of IPAMScope.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is IPAMScope {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === IPAMScope.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of the IPAM scope.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the IPAM this scope is a part of.
     */
    public /*out*/ readonly ipamArn!: pulumi.Output<string>;
    /**
     * The Id of the IPAM this scope is a part of.
     */
    public readonly ipamId!: pulumi.Output<string>;
    /**
     * Id of the IPAM scope.
     */
    public /*out*/ readonly ipamScopeId!: pulumi.Output<string>;
    /**
     * Determines whether this scope contains publicly routable space or space for a private network
     */
    public /*out*/ readonly ipamScopeType!: pulumi.Output<enums.ec2.IPAMScopeIpamScopeType>;
    /**
     * Is this one of the default scopes created with the IPAM.
     */
    public /*out*/ readonly isDefault!: pulumi.Output<boolean>;
    /**
     * The number of pools that currently exist in this scope.
     */
    public /*out*/ readonly poolCount!: pulumi.Output<number>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.ec2.IPAMScopeTag[] | undefined>;

    /**
     * Create a IPAMScope resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IPAMScopeArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.ipamId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ipamId'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["ipamId"] = args ? args.ipamId : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["ipamArn"] = undefined /*out*/;
            resourceInputs["ipamScopeId"] = undefined /*out*/;
            resourceInputs["ipamScopeType"] = undefined /*out*/;
            resourceInputs["isDefault"] = undefined /*out*/;
            resourceInputs["poolCount"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["ipamArn"] = undefined /*out*/;
            resourceInputs["ipamId"] = undefined /*out*/;
            resourceInputs["ipamScopeId"] = undefined /*out*/;
            resourceInputs["ipamScopeType"] = undefined /*out*/;
            resourceInputs["isDefault"] = undefined /*out*/;
            resourceInputs["poolCount"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(IPAMScope.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a IPAMScope resource.
 */
export interface IPAMScopeArgs {
    description?: pulumi.Input<string>;
    /**
     * The Id of the IPAM this scope is a part of.
     */
    ipamId: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.ec2.IPAMScopeTagArgs>[]>;
}

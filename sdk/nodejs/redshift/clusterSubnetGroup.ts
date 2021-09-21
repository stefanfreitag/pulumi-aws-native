// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Redshift::ClusterSubnetGroup
 *
 * @deprecated ClusterSubnetGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class ClusterSubnetGroup extends pulumi.CustomResource {
    /**
     * Get an existing ClusterSubnetGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ClusterSubnetGroup {
        pulumi.log.warn("ClusterSubnetGroup is deprecated: ClusterSubnetGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new ClusterSubnetGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:redshift:ClusterSubnetGroup';

    /**
     * Returns true if the given object is an instance of ClusterSubnetGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ClusterSubnetGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ClusterSubnetGroup.__pulumiType;
    }

    public readonly description!: pulumi.Output<string>;
    public readonly subnetIds!: pulumi.Output<string[]>;
    public readonly tags!: pulumi.Output<outputs.redshift.ClusterSubnetGroupTag[] | undefined>;

    /**
     * Create a ClusterSubnetGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated ClusterSubnetGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: ClusterSubnetGroupArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("ClusterSubnetGroup is deprecated: ClusterSubnetGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.description === undefined) && !opts.urn) {
                throw new Error("Missing required property 'description'");
            }
            if ((!args || args.subnetIds === undefined) && !opts.urn) {
                throw new Error("Missing required property 'subnetIds'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["subnetIds"] = args ? args.subnetIds : undefined;
            inputs["tags"] = args ? args.tags : undefined;
        } else {
            inputs["description"] = undefined /*out*/;
            inputs["subnetIds"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(ClusterSubnetGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a ClusterSubnetGroup resource.
 */
export interface ClusterSubnetGroupArgs {
    description: pulumi.Input<string>;
    subnetIds: pulumi.Input<pulumi.Input<string>[]>;
    tags?: pulumi.Input<pulumi.Input<inputs.redshift.ClusterSubnetGroupTagArgs>[]>;
}

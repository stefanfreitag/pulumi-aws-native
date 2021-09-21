// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Redshift::ClusterSecurityGroup
 *
 * @deprecated ClusterSecurityGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class ClusterSecurityGroup extends pulumi.CustomResource {
    /**
     * Get an existing ClusterSecurityGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ClusterSecurityGroup {
        pulumi.log.warn("ClusterSecurityGroup is deprecated: ClusterSecurityGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new ClusterSecurityGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:redshift:ClusterSecurityGroup';

    /**
     * Returns true if the given object is an instance of ClusterSecurityGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ClusterSecurityGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ClusterSecurityGroup.__pulumiType;
    }

    public readonly description!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.redshift.ClusterSecurityGroupTag[] | undefined>;

    /**
     * Create a ClusterSecurityGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated ClusterSecurityGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: ClusterSecurityGroupArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("ClusterSecurityGroup is deprecated: ClusterSecurityGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.description === undefined) && !opts.urn) {
                throw new Error("Missing required property 'description'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["tags"] = args ? args.tags : undefined;
        } else {
            inputs["description"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(ClusterSecurityGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a ClusterSecurityGroup resource.
 */
export interface ClusterSecurityGroupArgs {
    description: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.redshift.ClusterSecurityGroupTagArgs>[]>;
}

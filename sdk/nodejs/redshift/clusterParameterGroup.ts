// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Redshift::ClusterParameterGroup
 *
 * @deprecated ClusterParameterGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class ClusterParameterGroup extends pulumi.CustomResource {
    /**
     * Get an existing ClusterParameterGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ClusterParameterGroup {
        pulumi.log.warn("ClusterParameterGroup is deprecated: ClusterParameterGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new ClusterParameterGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:redshift:ClusterParameterGroup';

    /**
     * Returns true if the given object is an instance of ClusterParameterGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ClusterParameterGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ClusterParameterGroup.__pulumiType;
    }

    public readonly description!: pulumi.Output<string>;
    public readonly parameterGroupFamily!: pulumi.Output<string>;
    public readonly parameters!: pulumi.Output<outputs.redshift.ClusterParameterGroupParameter[] | undefined>;
    public readonly tags!: pulumi.Output<outputs.redshift.ClusterParameterGroupTag[] | undefined>;

    /**
     * Create a ClusterParameterGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated ClusterParameterGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: ClusterParameterGroupArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("ClusterParameterGroup is deprecated: ClusterParameterGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.description === undefined) && !opts.urn) {
                throw new Error("Missing required property 'description'");
            }
            if ((!args || args.parameterGroupFamily === undefined) && !opts.urn) {
                throw new Error("Missing required property 'parameterGroupFamily'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["parameterGroupFamily"] = args ? args.parameterGroupFamily : undefined;
            inputs["parameters"] = args ? args.parameters : undefined;
            inputs["tags"] = args ? args.tags : undefined;
        } else {
            inputs["description"] = undefined /*out*/;
            inputs["parameterGroupFamily"] = undefined /*out*/;
            inputs["parameters"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(ClusterParameterGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a ClusterParameterGroup resource.
 */
export interface ClusterParameterGroupArgs {
    description: pulumi.Input<string>;
    parameterGroupFamily: pulumi.Input<string>;
    parameters?: pulumi.Input<pulumi.Input<inputs.redshift.ClusterParameterGroupParameterArgs>[]>;
    tags?: pulumi.Input<pulumi.Input<inputs.redshift.ClusterParameterGroupTagArgs>[]>;
}

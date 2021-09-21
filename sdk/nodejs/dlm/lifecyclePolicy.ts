// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::DLM::LifecyclePolicy
 *
 * @deprecated LifecyclePolicy is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class LifecyclePolicy extends pulumi.CustomResource {
    /**
     * Get an existing LifecyclePolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): LifecyclePolicy {
        pulumi.log.warn("LifecyclePolicy is deprecated: LifecyclePolicy is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new LifecyclePolicy(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:dlm:LifecyclePolicy';

    /**
     * Returns true if the given object is an instance of LifecyclePolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is LifecyclePolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === LifecyclePolicy.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly executionRoleArn!: pulumi.Output<string | undefined>;
    public readonly policyDetails!: pulumi.Output<outputs.dlm.LifecyclePolicyPolicyDetails | undefined>;
    public readonly state!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<outputs.dlm.LifecyclePolicyTag[] | undefined>;

    /**
     * Create a LifecyclePolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated LifecyclePolicy is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args?: LifecyclePolicyArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("LifecyclePolicy is deprecated: LifecyclePolicy is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            inputs["description"] = args ? args.description : undefined;
            inputs["executionRoleArn"] = args ? args.executionRoleArn : undefined;
            inputs["policyDetails"] = args ? args.policyDetails : undefined;
            inputs["state"] = args ? args.state : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
        } else {
            inputs["arn"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["executionRoleArn"] = undefined /*out*/;
            inputs["policyDetails"] = undefined /*out*/;
            inputs["state"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(LifecyclePolicy.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a LifecyclePolicy resource.
 */
export interface LifecyclePolicyArgs {
    description?: pulumi.Input<string>;
    executionRoleArn?: pulumi.Input<string>;
    policyDetails?: pulumi.Input<inputs.dlm.LifecyclePolicyPolicyDetailsArgs>;
    state?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.dlm.LifecyclePolicyTagArgs>[]>;
}

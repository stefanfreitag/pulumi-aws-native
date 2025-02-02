// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::AutoScaling::WarmPool.
 */
export class WarmPool extends pulumi.CustomResource {
    /**
     * Get an existing WarmPool resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): WarmPool {
        return new WarmPool(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:autoscaling:WarmPool';

    /**
     * Returns true if the given object is an instance of WarmPool.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is WarmPool {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === WarmPool.__pulumiType;
    }

    public readonly autoScalingGroupName!: pulumi.Output<string>;
    public readonly instanceReusePolicy!: pulumi.Output<outputs.autoscaling.WarmPoolInstanceReusePolicy | undefined>;
    public readonly maxGroupPreparedCapacity!: pulumi.Output<number | undefined>;
    public readonly minSize!: pulumi.Output<number | undefined>;
    public readonly poolState!: pulumi.Output<string | undefined>;

    /**
     * Create a WarmPool resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: WarmPoolArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.autoScalingGroupName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'autoScalingGroupName'");
            }
            resourceInputs["autoScalingGroupName"] = args ? args.autoScalingGroupName : undefined;
            resourceInputs["instanceReusePolicy"] = args ? args.instanceReusePolicy : undefined;
            resourceInputs["maxGroupPreparedCapacity"] = args ? args.maxGroupPreparedCapacity : undefined;
            resourceInputs["minSize"] = args ? args.minSize : undefined;
            resourceInputs["poolState"] = args ? args.poolState : undefined;
        } else {
            resourceInputs["autoScalingGroupName"] = undefined /*out*/;
            resourceInputs["instanceReusePolicy"] = undefined /*out*/;
            resourceInputs["maxGroupPreparedCapacity"] = undefined /*out*/;
            resourceInputs["minSize"] = undefined /*out*/;
            resourceInputs["poolState"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["autoScalingGroupName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(WarmPool.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a WarmPool resource.
 */
export interface WarmPoolArgs {
    autoScalingGroupName: pulumi.Input<string>;
    instanceReusePolicy?: pulumi.Input<inputs.autoscaling.WarmPoolInstanceReusePolicyArgs>;
    maxGroupPreparedCapacity?: pulumi.Input<number>;
    minSize?: pulumi.Input<number>;
    poolState?: pulumi.Input<string>;
}

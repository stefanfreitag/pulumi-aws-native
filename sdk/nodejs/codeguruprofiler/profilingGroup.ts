// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * This resource schema represents the Profiling Group resource in the Amazon CodeGuru Profiler service.
 */
export class ProfilingGroup extends pulumi.CustomResource {
    /**
     * Get an existing ProfilingGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ProfilingGroup {
        return new ProfilingGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:codeguruprofiler:ProfilingGroup';

    /**
     * Returns true if the given object is an instance of ProfilingGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ProfilingGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ProfilingGroup.__pulumiType;
    }

    /**
     * The agent permissions attached to this profiling group.
     */
    public readonly agentPermissions!: pulumi.Output<any | undefined>;
    /**
     * Configuration for Notification Channels for Anomaly Detection feature in CodeGuru Profiler which enables customers to detect anomalies in the application profile for those methods that represent the highest proportion of CPU time or latency
     */
    public readonly anomalyDetectionNotificationConfiguration!: pulumi.Output<outputs.codeguruprofiler.ProfilingGroupChannel[] | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the specified profiling group.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The compute platform of the profiling group.
     */
    public readonly computePlatform!: pulumi.Output<enums.codeguruprofiler.ProfilingGroupComputePlatform | undefined>;
    /**
     * The name of the profiling group.
     */
    public readonly profilingGroupName!: pulumi.Output<string>;
    /**
     * The tags associated with a profiling group.
     */
    public readonly tags!: pulumi.Output<outputs.codeguruprofiler.ProfilingGroupTag[] | undefined>;

    /**
     * Create a ProfilingGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProfilingGroupArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.profilingGroupName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'profilingGroupName'");
            }
            inputs["agentPermissions"] = args ? args.agentPermissions : undefined;
            inputs["anomalyDetectionNotificationConfiguration"] = args ? args.anomalyDetectionNotificationConfiguration : undefined;
            inputs["computePlatform"] = args ? args.computePlatform : undefined;
            inputs["profilingGroupName"] = args ? args.profilingGroupName : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
        } else {
            inputs["agentPermissions"] = undefined /*out*/;
            inputs["anomalyDetectionNotificationConfiguration"] = undefined /*out*/;
            inputs["arn"] = undefined /*out*/;
            inputs["computePlatform"] = undefined /*out*/;
            inputs["profilingGroupName"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(ProfilingGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a ProfilingGroup resource.
 */
export interface ProfilingGroupArgs {
    /**
     * The agent permissions attached to this profiling group.
     */
    agentPermissions?: any;
    /**
     * Configuration for Notification Channels for Anomaly Detection feature in CodeGuru Profiler which enables customers to detect anomalies in the application profile for those methods that represent the highest proportion of CPU time or latency
     */
    anomalyDetectionNotificationConfiguration?: pulumi.Input<pulumi.Input<inputs.codeguruprofiler.ProfilingGroupChannelArgs>[]>;
    /**
     * The compute platform of the profiling group.
     */
    computePlatform?: pulumi.Input<enums.codeguruprofiler.ProfilingGroupComputePlatform>;
    /**
     * The name of the profiling group.
     */
    profilingGroupName: pulumi.Input<string>;
    /**
     * The tags associated with a profiling group.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.codeguruprofiler.ProfilingGroupTagArgs>[]>;
}

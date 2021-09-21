// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::AutoScaling::AutoScalingGroup
 *
 * @deprecated AutoScalingGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class AutoScalingGroup extends pulumi.CustomResource {
    /**
     * Get an existing AutoScalingGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): AutoScalingGroup {
        pulumi.log.warn("AutoScalingGroup is deprecated: AutoScalingGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new AutoScalingGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:autoscaling:AutoScalingGroup';

    /**
     * Returns true if the given object is an instance of AutoScalingGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AutoScalingGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AutoScalingGroup.__pulumiType;
    }

    public readonly autoScalingGroupName!: pulumi.Output<string | undefined>;
    public readonly availabilityZones!: pulumi.Output<string[] | undefined>;
    public readonly capacityRebalance!: pulumi.Output<boolean | undefined>;
    public readonly context!: pulumi.Output<string | undefined>;
    public readonly cooldown!: pulumi.Output<string | undefined>;
    public readonly desiredCapacity!: pulumi.Output<string | undefined>;
    public readonly healthCheckGracePeriod!: pulumi.Output<number | undefined>;
    public readonly healthCheckType!: pulumi.Output<string | undefined>;
    public readonly instanceId!: pulumi.Output<string | undefined>;
    public readonly launchConfigurationName!: pulumi.Output<string | undefined>;
    public readonly launchTemplate!: pulumi.Output<outputs.autoscaling.AutoScalingGroupLaunchTemplateSpecification | undefined>;
    public /*out*/ readonly launchTemplateSpecification!: pulumi.Output<string>;
    public readonly lifecycleHookSpecificationList!: pulumi.Output<outputs.autoscaling.AutoScalingGroupLifecycleHookSpecification[] | undefined>;
    public readonly loadBalancerNames!: pulumi.Output<string[] | undefined>;
    public readonly maxInstanceLifetime!: pulumi.Output<number | undefined>;
    public readonly maxSize!: pulumi.Output<string>;
    public readonly metricsCollection!: pulumi.Output<outputs.autoscaling.AutoScalingGroupMetricsCollection[] | undefined>;
    public readonly minSize!: pulumi.Output<string>;
    public readonly mixedInstancesPolicy!: pulumi.Output<outputs.autoscaling.AutoScalingGroupMixedInstancesPolicy | undefined>;
    public readonly newInstancesProtectedFromScaleIn!: pulumi.Output<boolean | undefined>;
    public readonly notificationConfigurations!: pulumi.Output<outputs.autoscaling.AutoScalingGroupNotificationConfiguration[] | undefined>;
    public readonly placementGroup!: pulumi.Output<string | undefined>;
    public readonly serviceLinkedRoleARN!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<outputs.autoscaling.AutoScalingGroupTagProperty[] | undefined>;
    public readonly targetGroupARNs!: pulumi.Output<string[] | undefined>;
    public readonly terminationPolicies!: pulumi.Output<string[] | undefined>;
    public readonly vPCZoneIdentifier!: pulumi.Output<string[] | undefined>;

    /**
     * Create a AutoScalingGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated AutoScalingGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: AutoScalingGroupArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("AutoScalingGroup is deprecated: AutoScalingGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.maxSize === undefined) && !opts.urn) {
                throw new Error("Missing required property 'maxSize'");
            }
            if ((!args || args.minSize === undefined) && !opts.urn) {
                throw new Error("Missing required property 'minSize'");
            }
            inputs["autoScalingGroupName"] = args ? args.autoScalingGroupName : undefined;
            inputs["availabilityZones"] = args ? args.availabilityZones : undefined;
            inputs["capacityRebalance"] = args ? args.capacityRebalance : undefined;
            inputs["context"] = args ? args.context : undefined;
            inputs["cooldown"] = args ? args.cooldown : undefined;
            inputs["desiredCapacity"] = args ? args.desiredCapacity : undefined;
            inputs["healthCheckGracePeriod"] = args ? args.healthCheckGracePeriod : undefined;
            inputs["healthCheckType"] = args ? args.healthCheckType : undefined;
            inputs["instanceId"] = args ? args.instanceId : undefined;
            inputs["launchConfigurationName"] = args ? args.launchConfigurationName : undefined;
            inputs["launchTemplate"] = args ? args.launchTemplate : undefined;
            inputs["lifecycleHookSpecificationList"] = args ? args.lifecycleHookSpecificationList : undefined;
            inputs["loadBalancerNames"] = args ? args.loadBalancerNames : undefined;
            inputs["maxInstanceLifetime"] = args ? args.maxInstanceLifetime : undefined;
            inputs["maxSize"] = args ? args.maxSize : undefined;
            inputs["metricsCollection"] = args ? args.metricsCollection : undefined;
            inputs["minSize"] = args ? args.minSize : undefined;
            inputs["mixedInstancesPolicy"] = args ? args.mixedInstancesPolicy : undefined;
            inputs["newInstancesProtectedFromScaleIn"] = args ? args.newInstancesProtectedFromScaleIn : undefined;
            inputs["notificationConfigurations"] = args ? args.notificationConfigurations : undefined;
            inputs["placementGroup"] = args ? args.placementGroup : undefined;
            inputs["serviceLinkedRoleARN"] = args ? args.serviceLinkedRoleARN : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["targetGroupARNs"] = args ? args.targetGroupARNs : undefined;
            inputs["terminationPolicies"] = args ? args.terminationPolicies : undefined;
            inputs["vPCZoneIdentifier"] = args ? args.vPCZoneIdentifier : undefined;
            inputs["launchTemplateSpecification"] = undefined /*out*/;
        } else {
            inputs["autoScalingGroupName"] = undefined /*out*/;
            inputs["availabilityZones"] = undefined /*out*/;
            inputs["capacityRebalance"] = undefined /*out*/;
            inputs["context"] = undefined /*out*/;
            inputs["cooldown"] = undefined /*out*/;
            inputs["desiredCapacity"] = undefined /*out*/;
            inputs["healthCheckGracePeriod"] = undefined /*out*/;
            inputs["healthCheckType"] = undefined /*out*/;
            inputs["instanceId"] = undefined /*out*/;
            inputs["launchConfigurationName"] = undefined /*out*/;
            inputs["launchTemplate"] = undefined /*out*/;
            inputs["launchTemplateSpecification"] = undefined /*out*/;
            inputs["lifecycleHookSpecificationList"] = undefined /*out*/;
            inputs["loadBalancerNames"] = undefined /*out*/;
            inputs["maxInstanceLifetime"] = undefined /*out*/;
            inputs["maxSize"] = undefined /*out*/;
            inputs["metricsCollection"] = undefined /*out*/;
            inputs["minSize"] = undefined /*out*/;
            inputs["mixedInstancesPolicy"] = undefined /*out*/;
            inputs["newInstancesProtectedFromScaleIn"] = undefined /*out*/;
            inputs["notificationConfigurations"] = undefined /*out*/;
            inputs["placementGroup"] = undefined /*out*/;
            inputs["serviceLinkedRoleARN"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["targetGroupARNs"] = undefined /*out*/;
            inputs["terminationPolicies"] = undefined /*out*/;
            inputs["vPCZoneIdentifier"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(AutoScalingGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a AutoScalingGroup resource.
 */
export interface AutoScalingGroupArgs {
    autoScalingGroupName?: pulumi.Input<string>;
    availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
    capacityRebalance?: pulumi.Input<boolean>;
    context?: pulumi.Input<string>;
    cooldown?: pulumi.Input<string>;
    desiredCapacity?: pulumi.Input<string>;
    healthCheckGracePeriod?: pulumi.Input<number>;
    healthCheckType?: pulumi.Input<string>;
    instanceId?: pulumi.Input<string>;
    launchConfigurationName?: pulumi.Input<string>;
    launchTemplate?: pulumi.Input<inputs.autoscaling.AutoScalingGroupLaunchTemplateSpecificationArgs>;
    lifecycleHookSpecificationList?: pulumi.Input<pulumi.Input<inputs.autoscaling.AutoScalingGroupLifecycleHookSpecificationArgs>[]>;
    loadBalancerNames?: pulumi.Input<pulumi.Input<string>[]>;
    maxInstanceLifetime?: pulumi.Input<number>;
    maxSize: pulumi.Input<string>;
    metricsCollection?: pulumi.Input<pulumi.Input<inputs.autoscaling.AutoScalingGroupMetricsCollectionArgs>[]>;
    minSize: pulumi.Input<string>;
    mixedInstancesPolicy?: pulumi.Input<inputs.autoscaling.AutoScalingGroupMixedInstancesPolicyArgs>;
    newInstancesProtectedFromScaleIn?: pulumi.Input<boolean>;
    notificationConfigurations?: pulumi.Input<pulumi.Input<inputs.autoscaling.AutoScalingGroupNotificationConfigurationArgs>[]>;
    placementGroup?: pulumi.Input<string>;
    serviceLinkedRoleARN?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.autoscaling.AutoScalingGroupTagPropertyArgs>[]>;
    targetGroupARNs?: pulumi.Input<pulumi.Input<string>[]>;
    terminationPolicies?: pulumi.Input<pulumi.Input<string>[]>;
    vPCZoneIdentifier?: pulumi.Input<pulumi.Input<string>[]>;
}

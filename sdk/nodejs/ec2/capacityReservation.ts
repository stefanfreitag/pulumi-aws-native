// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::CapacityReservation
 *
 * @deprecated CapacityReservation is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class CapacityReservation extends pulumi.CustomResource {
    /**
     * Get an existing CapacityReservation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): CapacityReservation {
        pulumi.log.warn("CapacityReservation is deprecated: CapacityReservation is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new CapacityReservation(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:CapacityReservation';

    /**
     * Returns true if the given object is an instance of CapacityReservation.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CapacityReservation {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CapacityReservation.__pulumiType;
    }

    public readonly availabilityZone!: pulumi.Output<string>;
    public /*out*/ readonly availableInstanceCount!: pulumi.Output<number>;
    public readonly ebsOptimized!: pulumi.Output<boolean | undefined>;
    public readonly endDate!: pulumi.Output<string | undefined>;
    public readonly endDateType!: pulumi.Output<string | undefined>;
    public readonly ephemeralStorage!: pulumi.Output<boolean | undefined>;
    public readonly instanceCount!: pulumi.Output<number>;
    public readonly instanceMatchCriteria!: pulumi.Output<string | undefined>;
    public readonly instancePlatform!: pulumi.Output<string>;
    public readonly instanceType!: pulumi.Output<string>;
    public readonly tagSpecifications!: pulumi.Output<outputs.ec2.CapacityReservationTagSpecification[] | undefined>;
    public readonly tenancy!: pulumi.Output<string | undefined>;
    public /*out*/ readonly totalInstanceCount!: pulumi.Output<number>;

    /**
     * Create a CapacityReservation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated CapacityReservation is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: CapacityReservationArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("CapacityReservation is deprecated: CapacityReservation is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.availabilityZone === undefined) && !opts.urn) {
                throw new Error("Missing required property 'availabilityZone'");
            }
            if ((!args || args.instanceCount === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceCount'");
            }
            if ((!args || args.instancePlatform === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instancePlatform'");
            }
            if ((!args || args.instanceType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceType'");
            }
            inputs["availabilityZone"] = args ? args.availabilityZone : undefined;
            inputs["ebsOptimized"] = args ? args.ebsOptimized : undefined;
            inputs["endDate"] = args ? args.endDate : undefined;
            inputs["endDateType"] = args ? args.endDateType : undefined;
            inputs["ephemeralStorage"] = args ? args.ephemeralStorage : undefined;
            inputs["instanceCount"] = args ? args.instanceCount : undefined;
            inputs["instanceMatchCriteria"] = args ? args.instanceMatchCriteria : undefined;
            inputs["instancePlatform"] = args ? args.instancePlatform : undefined;
            inputs["instanceType"] = args ? args.instanceType : undefined;
            inputs["tagSpecifications"] = args ? args.tagSpecifications : undefined;
            inputs["tenancy"] = args ? args.tenancy : undefined;
            inputs["availableInstanceCount"] = undefined /*out*/;
            inputs["totalInstanceCount"] = undefined /*out*/;
        } else {
            inputs["availabilityZone"] = undefined /*out*/;
            inputs["availableInstanceCount"] = undefined /*out*/;
            inputs["ebsOptimized"] = undefined /*out*/;
            inputs["endDate"] = undefined /*out*/;
            inputs["endDateType"] = undefined /*out*/;
            inputs["ephemeralStorage"] = undefined /*out*/;
            inputs["instanceCount"] = undefined /*out*/;
            inputs["instanceMatchCriteria"] = undefined /*out*/;
            inputs["instancePlatform"] = undefined /*out*/;
            inputs["instanceType"] = undefined /*out*/;
            inputs["tagSpecifications"] = undefined /*out*/;
            inputs["tenancy"] = undefined /*out*/;
            inputs["totalInstanceCount"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(CapacityReservation.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a CapacityReservation resource.
 */
export interface CapacityReservationArgs {
    availabilityZone: pulumi.Input<string>;
    ebsOptimized?: pulumi.Input<boolean>;
    endDate?: pulumi.Input<string>;
    endDateType?: pulumi.Input<string>;
    ephemeralStorage?: pulumi.Input<boolean>;
    instanceCount: pulumi.Input<number>;
    instanceMatchCriteria?: pulumi.Input<string>;
    instancePlatform: pulumi.Input<string>;
    instanceType: pulumi.Input<string>;
    tagSpecifications?: pulumi.Input<pulumi.Input<inputs.ec2.CapacityReservationTagSpecificationArgs>[]>;
    tenancy?: pulumi.Input<string>;
}

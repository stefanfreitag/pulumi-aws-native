// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Schema describing various properties for ECS TaskDefinition
 */
export class TaskDefinition extends pulumi.CustomResource {
    /**
     * Get an existing TaskDefinition resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): TaskDefinition {
        return new TaskDefinition(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ecs:TaskDefinition';

    /**
     * Returns true if the given object is an instance of TaskDefinition.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TaskDefinition {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TaskDefinition.__pulumiType;
    }

    public readonly containerDefinitions!: pulumi.Output<outputs.ecs.TaskDefinitionContainerDefinition[] | undefined>;
    public readonly cpu!: pulumi.Output<string | undefined>;
    public readonly ephemeralStorage!: pulumi.Output<outputs.ecs.TaskDefinitionEphemeralStorage | undefined>;
    public readonly executionRoleArn!: pulumi.Output<string | undefined>;
    public readonly family!: pulumi.Output<string | undefined>;
    public readonly inferenceAccelerators!: pulumi.Output<outputs.ecs.TaskDefinitionInferenceAccelerator[] | undefined>;
    public readonly ipcMode!: pulumi.Output<string | undefined>;
    public readonly memory!: pulumi.Output<string | undefined>;
    public readonly networkMode!: pulumi.Output<string | undefined>;
    public readonly pidMode!: pulumi.Output<string | undefined>;
    public readonly placementConstraints!: pulumi.Output<outputs.ecs.TaskDefinitionTaskDefinitionPlacementConstraint[] | undefined>;
    public readonly proxyConfiguration!: pulumi.Output<outputs.ecs.TaskDefinitionProxyConfiguration | undefined>;
    public readonly requiresCompatibilities!: pulumi.Output<string[] | undefined>;
    public readonly tags!: pulumi.Output<outputs.ecs.TaskDefinitionTag[] | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the Amazon ECS task definition
     */
    public /*out*/ readonly taskDefinitionArn!: pulumi.Output<string>;
    public readonly taskRoleArn!: pulumi.Output<string | undefined>;
    public readonly volumes!: pulumi.Output<outputs.ecs.TaskDefinitionVolume[] | undefined>;

    /**
     * Create a TaskDefinition resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: TaskDefinitionArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            inputs["containerDefinitions"] = args ? args.containerDefinitions : undefined;
            inputs["cpu"] = args ? args.cpu : undefined;
            inputs["ephemeralStorage"] = args ? args.ephemeralStorage : undefined;
            inputs["executionRoleArn"] = args ? args.executionRoleArn : undefined;
            inputs["family"] = args ? args.family : undefined;
            inputs["inferenceAccelerators"] = args ? args.inferenceAccelerators : undefined;
            inputs["ipcMode"] = args ? args.ipcMode : undefined;
            inputs["memory"] = args ? args.memory : undefined;
            inputs["networkMode"] = args ? args.networkMode : undefined;
            inputs["pidMode"] = args ? args.pidMode : undefined;
            inputs["placementConstraints"] = args ? args.placementConstraints : undefined;
            inputs["proxyConfiguration"] = args ? args.proxyConfiguration : undefined;
            inputs["requiresCompatibilities"] = args ? args.requiresCompatibilities : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["taskRoleArn"] = args ? args.taskRoleArn : undefined;
            inputs["volumes"] = args ? args.volumes : undefined;
            inputs["taskDefinitionArn"] = undefined /*out*/;
        } else {
            inputs["containerDefinitions"] = undefined /*out*/;
            inputs["cpu"] = undefined /*out*/;
            inputs["ephemeralStorage"] = undefined /*out*/;
            inputs["executionRoleArn"] = undefined /*out*/;
            inputs["family"] = undefined /*out*/;
            inputs["inferenceAccelerators"] = undefined /*out*/;
            inputs["ipcMode"] = undefined /*out*/;
            inputs["memory"] = undefined /*out*/;
            inputs["networkMode"] = undefined /*out*/;
            inputs["pidMode"] = undefined /*out*/;
            inputs["placementConstraints"] = undefined /*out*/;
            inputs["proxyConfiguration"] = undefined /*out*/;
            inputs["requiresCompatibilities"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["taskDefinitionArn"] = undefined /*out*/;
            inputs["taskRoleArn"] = undefined /*out*/;
            inputs["volumes"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(TaskDefinition.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a TaskDefinition resource.
 */
export interface TaskDefinitionArgs {
    containerDefinitions?: pulumi.Input<pulumi.Input<inputs.ecs.TaskDefinitionContainerDefinitionArgs>[]>;
    cpu?: pulumi.Input<string>;
    ephemeralStorage?: pulumi.Input<inputs.ecs.TaskDefinitionEphemeralStorageArgs>;
    executionRoleArn?: pulumi.Input<string>;
    family?: pulumi.Input<string>;
    inferenceAccelerators?: pulumi.Input<pulumi.Input<inputs.ecs.TaskDefinitionInferenceAcceleratorArgs>[]>;
    ipcMode?: pulumi.Input<string>;
    memory?: pulumi.Input<string>;
    networkMode?: pulumi.Input<string>;
    pidMode?: pulumi.Input<string>;
    placementConstraints?: pulumi.Input<pulumi.Input<inputs.ecs.TaskDefinitionTaskDefinitionPlacementConstraintArgs>[]>;
    proxyConfiguration?: pulumi.Input<inputs.ecs.TaskDefinitionProxyConfigurationArgs>;
    requiresCompatibilities?: pulumi.Input<pulumi.Input<string>[]>;
    tags?: pulumi.Input<pulumi.Input<inputs.ecs.TaskDefinitionTagArgs>[]>;
    taskRoleArn?: pulumi.Input<string>;
    volumes?: pulumi.Input<pulumi.Input<inputs.ecs.TaskDefinitionVolumeArgs>[]>;
}

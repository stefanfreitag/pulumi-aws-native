// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Creates a gateway task definition.
 */
export function getTaskDefinition(args: GetTaskDefinitionArgs, opts?: pulumi.InvokeOptions): Promise<GetTaskDefinitionResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:iotwireless:getTaskDefinition", {
        "id": args.id,
    }, opts);
}

export interface GetTaskDefinitionArgs {
    /**
     * The ID of the new wireless gateway task definition
     */
    id: string;
}

export interface GetTaskDefinitionResult {
    /**
     * TaskDefinition arn. Returned after successful create.
     */
    readonly arn?: string;
    /**
     * Whether to automatically create tasks using this task definition for all gateways with the specified current version. If false, the task must me created by calling CreateWirelessGatewayTask.
     */
    readonly autoCreateTasks?: boolean;
    /**
     * The ID of the new wireless gateway task definition
     */
    readonly id?: string;
    /**
     * The list of task definitions.
     */
    readonly loRaWANUpdateGatewayTaskEntry?: outputs.iotwireless.TaskDefinitionLoRaWANUpdateGatewayTaskEntry;
    /**
     * The name of the new resource.
     */
    readonly name?: string;
    /**
     * A list of key-value pairs that contain metadata for the destination.
     */
    readonly tags?: outputs.iotwireless.TaskDefinitionTag[];
    /**
     * A filter to list only the wireless gateway task definitions that use this task definition type
     */
    readonly taskDefinitionType?: enums.iotwireless.TaskDefinitionType;
    /**
     * Information about the gateways to update.
     */
    readonly update?: outputs.iotwireless.TaskDefinitionUpdateWirelessGatewayTaskCreate;
}
/**
 * Creates a gateway task definition.
 */
export function getTaskDefinitionOutput(args: GetTaskDefinitionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetTaskDefinitionResult> {
    return pulumi.output(args).apply((a: any) => getTaskDefinition(a, opts))
}

export interface GetTaskDefinitionOutputArgs {
    /**
     * The ID of the new wireless gateway task definition
     */
    id: pulumi.Input<string>;
}

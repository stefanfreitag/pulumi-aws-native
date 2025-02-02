// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::IoTEvents::Input resource creates an input. To monitor your devices and processes, they must have a way to get telemetry data into AWS IoT Events. This is done by sending messages as *inputs* to AWS IoT Events. For more information, see [How to Use AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*.
 */
export function getInput(args: GetInputArgs, opts?: pulumi.InvokeOptions): Promise<GetInputResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:iotevents:getInput", {
        "inputName": args.inputName,
    }, opts);
}

export interface GetInputArgs {
    /**
     * The name of the input.
     */
    inputName: string;
}

export interface GetInputResult {
    readonly inputDefinition?: outputs.iotevents.InputDefinition;
    /**
     * A brief description of the input.
     */
    readonly inputDescription?: string;
    /**
     * An array of key-value pairs to apply to this resource.
     *
     * For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
     */
    readonly tags?: outputs.Tag[];
}
/**
 * The AWS::IoTEvents::Input resource creates an input. To monitor your devices and processes, they must have a way to get telemetry data into AWS IoT Events. This is done by sending messages as *inputs* to AWS IoT Events. For more information, see [How to Use AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*.
 */
export function getInputOutput(args: GetInputOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetInputResult> {
    return pulumi.output(args).apply((a: any) => getInput(a, opts))
}

export interface GetInputOutputArgs {
    /**
     * The name of the input.
     */
    inputName: pulumi.Input<string>;
}

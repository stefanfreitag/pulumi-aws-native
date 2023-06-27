// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Represents a studio component that connects a non-Nimble Studio resource in your account to your studio
 */
export function getStudioComponent(args: GetStudioComponentArgs, opts?: pulumi.InvokeOptions): Promise<GetStudioComponentResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:nimblestudio:getStudioComponent", {
        "studioComponentId": args.studioComponentId,
        "studioId": args.studioId,
    }, opts);
}

export interface GetStudioComponentArgs {
    studioComponentId: string;
    /**
     * <p>The studio ID. </p>
     */
    studioId: string;
}

export interface GetStudioComponentResult {
    readonly configuration?: outputs.nimblestudio.StudioComponentConfiguration;
    /**
     * <p>The description.</p>
     */
    readonly description?: string;
    /**
     * <p>The EC2 security groups that control access to the studio component.</p>
     */
    readonly ec2SecurityGroupIds?: string[];
    /**
     * <p>Initialization scripts for studio components.</p>
     */
    readonly initializationScripts?: outputs.nimblestudio.StudioComponentInitializationScript[];
    /**
     * <p>The name for the studio component.</p>
     */
    readonly name?: string;
    readonly runtimeRoleArn?: string;
    /**
     * <p>Parameters for the studio component scripts.</p>
     */
    readonly scriptParameters?: outputs.nimblestudio.StudioComponentScriptParameterKeyValue[];
    readonly secureInitializationRoleArn?: string;
    readonly studioComponentId?: string;
    readonly type?: enums.nimblestudio.StudioComponentType;
}
/**
 * Represents a studio component that connects a non-Nimble Studio resource in your account to your studio
 */
export function getStudioComponentOutput(args: GetStudioComponentOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetStudioComponentResult> {
    return pulumi.output(args).apply((a: any) => getStudioComponent(a, opts))
}

export interface GetStudioComponentOutputArgs {
    studioComponentId: pulumi.Input<string>;
    /**
     * <p>The studio ID. </p>
     */
    studioId: pulumi.Input<string>;
}

// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Definition of AWS::AmplifyUIBuilder::Component Resource Type
 */
export function getComponent(args: GetComponentArgs, opts?: pulumi.InvokeOptions): Promise<GetComponentResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:amplifyuibuilder:getComponent", {
        "appId": args.appId,
        "environmentName": args.environmentName,
        "id": args.id,
    }, opts);
}

export interface GetComponentArgs {
    appId: string;
    environmentName: string;
    id: string;
}

export interface GetComponentResult {
    readonly bindingProperties?: {[key: string]: outputs.amplifyuibuilder.ComponentBindingPropertiesValue};
    readonly children?: outputs.amplifyuibuilder.ComponentChild[];
    readonly collectionProperties?: {[key: string]: outputs.amplifyuibuilder.ComponentDataConfiguration};
    readonly componentType?: string;
    readonly createdAt?: string;
    readonly events?: {[key: string]: outputs.amplifyuibuilder.ComponentEvent};
    readonly id?: string;
    readonly modifiedAt?: string;
    readonly name?: string;
    readonly overrides?: {[key: string]: any};
    readonly properties?: {[key: string]: outputs.amplifyuibuilder.ComponentProperty};
    readonly schemaVersion?: string;
    readonly sourceId?: string;
    readonly tags?: {[key: string]: string};
    readonly variants?: outputs.amplifyuibuilder.ComponentVariant[];
}
/**
 * Definition of AWS::AmplifyUIBuilder::Component Resource Type
 */
export function getComponentOutput(args: GetComponentOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetComponentResult> {
    return pulumi.output(args).apply((a: any) => getComponent(a, opts))
}

export interface GetComponentOutputArgs {
    appId: pulumi.Input<string>;
    environmentName: pulumi.Input<string>;
    id: pulumi.Input<string>;
}

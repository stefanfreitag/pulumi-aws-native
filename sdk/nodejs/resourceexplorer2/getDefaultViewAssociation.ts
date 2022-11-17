// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Definition of AWS::ResourceExplorer2::DefaultViewAssociation Resource Type
 */
export function getDefaultViewAssociation(args: GetDefaultViewAssociationArgs, opts?: pulumi.InvokeOptions): Promise<GetDefaultViewAssociationResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:resourceexplorer2:getDefaultViewAssociation", {
        "associatedAwsPrincipal": args.associatedAwsPrincipal,
    }, opts);
}

export interface GetDefaultViewAssociationArgs {
    /**
     * The AWS principal that the default view is associated with, used as the unique identifier for this resource.
     */
    associatedAwsPrincipal: string;
}

export interface GetDefaultViewAssociationResult {
    /**
     * The AWS principal that the default view is associated with, used as the unique identifier for this resource.
     */
    readonly associatedAwsPrincipal?: string;
    readonly viewArn?: string;
}

export function getDefaultViewAssociationOutput(args: GetDefaultViewAssociationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDefaultViewAssociationResult> {
    return pulumi.output(args).apply(a => getDefaultViewAssociation(a, opts))
}

export interface GetDefaultViewAssociationOutputArgs {
    /**
     * The AWS principal that the default view is associated with, used as the unique identifier for this resource.
     */
    associatedAwsPrincipal: pulumi.Input<string>;
}

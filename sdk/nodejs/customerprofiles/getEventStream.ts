// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * An Event Stream resource of Amazon Connect Customer Profiles
 */
export function getEventStream(args: GetEventStreamArgs, opts?: pulumi.InvokeOptions): Promise<GetEventStreamResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:customerprofiles:getEventStream", {
        "domainName": args.domainName,
        "eventStreamName": args.eventStreamName,
    }, opts);
}

export interface GetEventStreamArgs {
    /**
     * The unique name of the domain.
     */
    domainName: string;
    /**
     * The name of the event stream.
     */
    eventStreamName: string;
}

export interface GetEventStreamResult {
    /**
     * The timestamp of when the export was created.
     */
    readonly createdAt?: string;
    /**
     * Details regarding the Kinesis stream.
     */
    readonly destinationDetails?: outputs.customerprofiles.DestinationDetailsProperties;
    /**
     * A unique identifier for the event stream.
     */
    readonly eventStreamArn?: string;
    /**
     * The operational state of destination stream for export.
     */
    readonly state?: enums.customerprofiles.EventStreamState;
    /**
     * The tags used to organize, track, or control access for this resource.
     */
    readonly tags?: outputs.Tag[];
}
/**
 * An Event Stream resource of Amazon Connect Customer Profiles
 */
export function getEventStreamOutput(args: GetEventStreamOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetEventStreamResult> {
    return pulumi.output(args).apply((a: any) => getEventStream(a, opts))
}

export interface GetEventStreamOutputArgs {
    /**
     * The unique name of the domain.
     */
    domainName: pulumi.Input<string>;
    /**
     * The name of the event stream.
     */
    eventStreamName: pulumi.Input<string>;
}

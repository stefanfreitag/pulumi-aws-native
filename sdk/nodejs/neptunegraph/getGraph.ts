// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::NeptuneGraph::Graph resource creates an Amazon NeptuneGraph Graph.
 */
export function getGraph(args: GetGraphArgs, opts?: pulumi.InvokeOptions): Promise<GetGraphResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:neptunegraph:getGraph", {
        "graphId": args.graphId,
    }, opts);
}

export interface GetGraphArgs {
    /**
     * The auto-generated id assigned by the service.
     */
    graphId: string;
}

export interface GetGraphResult {
    /**
     * Value that indicates whether the Graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.
     *
     * _Default_: If not specified, the default value is true.
     */
    readonly deletionProtection?: boolean;
    /**
     * The connection endpoint for the graph. For example: `g-12a3bcdef4.us-east-1.neptune-graph.amazonaws.com`
     */
    readonly endpoint?: string;
    /**
     * Graph resource ARN
     */
    readonly graphArn?: string;
    /**
     * The auto-generated id assigned by the service.
     */
    readonly graphId?: string;
    /**
     * Memory for the Graph.
     */
    readonly provisionedMemory?: number;
    /**
     * Specifies whether the Graph can be reached over the internet. Access to all graphs requires IAM authentication.
     *
     * When the Graph is publicly reachable, its Domain Name System (DNS) endpoint resolves to the public IP address from the internet.
     *
     * When the Graph isn't publicly reachable, you need to create a PrivateGraphEndpoint in a given VPC to ensure the DNS name resolves to a private IP address that is reachable from the VPC.
     *
     * _Default_: If not specified, the default value is false.
     */
    readonly publicConnectivity?: boolean;
    /**
     * The tags associated with this graph.
     */
    readonly tags?: outputs.Tag[];
}
/**
 * The AWS::NeptuneGraph::Graph resource creates an Amazon NeptuneGraph Graph.
 */
export function getGraphOutput(args: GetGraphOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetGraphResult> {
    return pulumi.output(args).apply((a: any) => getGraph(a, opts))
}

export interface GetGraphOutputArgs {
    /**
     * The auto-generated id assigned by the service.
     */
    graphId: pulumi.Input<string>;
}
